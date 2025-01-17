package services

import (
	"context"
	"fmt"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/serializers"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/services/3rd/eth"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/services/3rd/zkclient"
	"github.com/ethereum/go-ethereum/core/types"
	"math/big"
	"strconv"
	"strings"

	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/services/3rd/binds/aikb721"
	"github.com/ethereum/go-ethereum/accounts/abi"
	"github.com/ethereum/go-ethereum/common"

	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/errs"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/logger"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/models"
	"go.uber.org/zap"
)

func (s *Service) JobCreateAgentKnowledgeBase(ctx context.Context) error {
	err := s.JobRunCheck(
		ctx, "JobCreateAgentKnowledgeBase",
		func() error {
			return s.CreateAgentKnowledgeBase(ctx)
		},
	)
	if err != nil {
		return errs.NewError(err)
	}
	return nil
}

func (s *Service) CreateAgentKnowledgeBase(ctx context.Context) error {
	list, err := s.KnowledgeUsecase.GetKnowledgeBaseByStatus(ctx, models.KnowledgeBaseStatusDone, 0, 10)
	if err != nil {
		return err
	}
	for _, item := range list {
		err = s.DeployAgentKnowledgeBase(ctx, item)
		if err != nil {
			logger.Info("JobCreateAgentKnowledgeBase", "CreateAgentKnowledgeBase",
				zap.Any("err", err), zap.Any("kb", item))
			s.SendTeleMsgToKBChannel(ctx, fmt.Sprintf("CreateAgentKnowledgeBase \n err:%v \nknowledge_base_id:%v", err.Error(), item.ID), s.conf.KnowledgeBaseConfig.KBErrorTelegramAlert)
		}
	}
	list, err = s.KnowledgeUsecase.GetManyKnowledgeBaseByQuery(ctx, fmt.Sprintf("status = '%v' AND filecoin_hash <> '' AND kb_id <> '' ", models.KnowledgeBaseStatusPaymentReceipt), "id asc", 0, 10)
	if err != nil {
		return err
	}
	for _, item := range list {
		err = s.DeployAgentKnowledgeBase(ctx, item)
		if err != nil {
			logger.Info("JobCreateAgentKnowledgeBase", "CreateAgentKnowledgeBase",
				zap.Any("err", err), zap.Any("kb", item))
			s.SendTeleMsgToKBChannel(ctx, fmt.Sprintf("CreateAgentKnowledgeBase \n err:%v \nknowledge_base_id:%v", err.Error(), item.ID), s.conf.KnowledgeBaseConfig.KBErrorTelegramAlert)
		}
	}
	return nil
}

func (s *Service) DeployAgentKnowledgeBase(ctx context.Context, info *models.KnowledgeBase) error {
	if len(info.FilecoinHash) == 0 {
		return fmt.Errorf("file coin hash is empty")
	}
	if len(info.KBTokenID) > 0 {
		oldStatus := info.Status
		info.Status = models.KnowledgeBaseStatusMinted
		err := s.KnowledgeUsecase.UpdateKnowledgeBaseById(ctx, info.ID, map[string]interface{}{
			"status": info.Status,
		})
		if err != nil {
			return fmt.Errorf("UpdateKnowledgeBaseById: %v", err)
		}
		s.SendTeleMsgToKBChannel(ctx,
			fmt.Sprintf("Update KB Status \n kb_id:%v \n old_status:%v \n new_status:%v \n mint id :%v \n tx:%v",
				info.ID, oldStatus, info.Status, info.KBTokenID, info.KBTokenMintTx),
			s.conf.KnowledgeBaseConfig.KBActivitiesTelegramAlert)
		return nil
	}
	appConfig, err := s.AppConfigUseCase.GetAllNameValueInAppConfig(ctx, strconv.FormatUint(info.NetworkID, 10))
	if err != nil {
		return fmt.Errorf("error when get all name value in app config: %v", err)
	}
	priKey := appConfig[models.KeyConfigNameWalletDeploy]
	if len(priKey) == 0 {
		return fmt.Errorf("error when no priKey for network %v", info.NetworkID)
	}
	_, pubKey, err := eth.GetAccountInfo(priKey)
	if err != nil {
		return fmt.Errorf("error when get account info: %v", err)
	}
	kbWorkerHubAddress := appConfig[models.KeyConfigNameKnowledgeBaseWorkerHubAddress]
	if len(kbWorkerHubAddress) == 0 {
		return fmt.Errorf("error when no KnowledgeBaseWorkerHubAddress for network %v", info.NetworkID)
	}
	modelId := appConfig[models.KeyConfigNameModelId]
	if len(modelId) == 0 {
		return fmt.Errorf("error not found model id , network %v", info.NetworkID)
	}
	tokenContractAddress := appConfig[models.KeyConfigNameKnowledgeBaseTokenContractAddress]
	if len(tokenContractAddress) == 0 {
		return fmt.Errorf("error not found tokenContractAddress , network %v", info.NetworkID)
	}

	instanceABI, err := abi.JSON(strings.NewReader(aikb721.EternalAIKB721MetaData.ABI))
	if err != nil {
		return fmt.Errorf("error failed to read ABI JSON: %v", err)
	}

	uri := info.FilecoinHash
	data := []byte(info.FilecoinHash)
	promptKey := "KnowledgeBaseAgent"
	fee := big.NewInt(0)
	modelIdUint32, err := strconv.ParseUint(modelId, 10, 32)
	dataBytes, err := instanceABI.Pack(
		"mint", common.HexToAddress(info.UserAddress),
		uri,
		data,
		fee,
		promptKey,
		common.HexToAddress(kbWorkerHubAddress),
		uint32(modelIdUint32),
	)
	//to common.Address, data []byte,   promptScheduler common.Address, modelId uint32
	if err != nil {
		return fmt.Errorf("error: failed to pack ABI data: %v", err)
	}

	rpc := s.conf.GetConfigKeyString(
		info.NetworkID,
		"rpc_url",
	)
	var paymasterAddress, paymasterToken string
	var paymasterFeeZero bool
	if s.conf.ExistsedConfigKey(info.NetworkID, "paymaster_address") &&
		s.conf.ExistsedConfigKey(info.NetworkID, "paymaster_token") {
		paymasterAddress = s.conf.GetConfigKeyString(info.NetworkID, "paymaster_address")
		paymasterToken = s.conf.GetConfigKeyString(info.NetworkID, "paymaster_token")
		paymasterFeeZero = s.conf.GetConfigKeyBool(info.NetworkID, "paymaster_fee_zero")
	}
	aiZkClient := zkclient.NewZkClient(rpc,
		paymasterFeeZero,
		paymasterAddress,
		paymasterToken)

	tx, err := aiZkClient.Transact(priKey, *pubKey, common.HexToAddress(tokenContractAddress), big.NewInt(0), dataBytes)
	if err != nil {
		return fmt.Errorf("error: failed to transact: %v", err)
	}
	if tx == nil {
		return fmt.Errorf("error: can find tx receipt ")
	}
	contract, err := aikb721.NewEternalAIKB721(common.HexToAddress(tokenContractAddress), nil)
	if err != nil {
		return fmt.Errorf("error: failed to new either contract: %v", err)
	}
	tokenId := ""
	for _, log := range tx.Receipt.Logs {
		inferData, err := contract.ParseNewToken(*log)
		if err == nil {
			tokenId = inferData.TokenId.String()
			break
		}
	}
	if len(tokenId) == 0 {
		return fmt.Errorf("error: no token id found in tx receipt :%v", tx.TxHash.Hex())
	}
	oldStatus := info.Status
	info.KBTokenID = tokenId
	info.KBTokenContractAddress = tokenContractAddress
	info.KBTokenMintTx = strings.ToLower(tx.TxHash.Hex())
	info.Status = models.KnowledgeBaseStatusMinted
	err = s.KnowledgeUsecase.UpdateKnowledgeBaseById(ctx, info.ID, map[string]interface{}{
		"status":                    info.Status,
		"kb_token_id":               info.KBTokenID,
		"kb_token_contract_address": info.KBTokenContractAddress,
		"kb_token_mint_tx":          info.KBTokenMintTx,
	})
	if err != nil {
		return fmt.Errorf("error: failed to update knowledge base status: %v", err)
	}
	s.SendTeleMsgToKBChannel(ctx,
		fmt.Sprintf("Update KB Status \n kb_id:%v \n old_status:%v \n new_status:%v \n mint id :%v \n tx:%v",
			info.ID, oldStatus, info.Status, info.KBTokenID, info.KBTokenMintTx),
		s.conf.KnowledgeBaseConfig.KBActivitiesTelegramAlert)
	err = s.AgentInfoUseCase.UpdateAgentInfoById(ctx, info.AgentInfoId,
		map[string]interface{}{
			"status":                 models.AssistantStatusReady,
			"agent_contract_id":      tokenId,
			"agent_contract_address": info.KBTokenContractAddress,
			"agent_nft_minted":       true,
		})
	if err != nil {
		return fmt.Errorf("error: failed to update agent info: %v", err)
	}
	return nil
}

func (s *Service) UpdateKnowledgeBaseInContractWithSignature(ctx context.Context, info *models.KnowledgeBase, request *serializers.UpdateKnowledgeBaseWithSignatureRequest) (*models.KnowledgeBase, error) {
	var err error
	appConfig, err := s.AppConfigUseCase.GetAllNameValueInAppConfig(ctx, request.NetworkID)
	if err != nil {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: get all name value in app config: %v", err)
	}
	priKey := appConfig[models.KeyConfigNameWalletDeploy]
	if len(priKey) == 0 {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: no priKey for network %v", request.NetworkID)
	}
	kbWorkerHubAddress := appConfig[models.KeyConfigNameKnowledgeBaseWorkerHubAddress]
	if len(kbWorkerHubAddress) == 0 {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: no KnowledgeBaseWorkerHubAddress for network %v", request.NetworkID)
	}
	tokenContractAddress := appConfig[models.KeyConfigNameKnowledgeBaseTokenContractAddress]
	if len(tokenContractAddress) == 0 {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: no tokenContractAddress for network %v", request.NetworkID)
	}

	instanceABI, err := abi.JSON(strings.NewReader(aikb721.EternalAIKB721MetaData.ABI))
	if err != nil {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: failed to read ABI JSON: %v", err)
	}
	kbId, ok := new(big.Int).SetString(request.KnowledgeBaseId, 10)
	if !ok {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: knowledge_base_id is nnot big int")
	}
	//agentId *big.Int, sysPrompt []byte, promptKey string, promptIdx *big.Int, randomNonce *big.Int, signature []byte
	signature := request.SignatureData
	if strings.HasPrefix(signature, "0x") {
		signature = strings.TrimPrefix(signature, "0x")
	}
	dataBytes, err := instanceABI.Pack(
		"updateAgentDataWithSignature", kbId,
		[]byte(request.HashData),
		request.PromptKeyData,
		big.NewInt(0),
		request.RandomNonceData,
		common.Hex2Bytes(signature),
	)
	//to common.Address, data []byte,   promptScheduler common.Address, modelId uint32
	if err != nil {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: failed to pack ABI data: %v", err)
	}
	networkId, _ := strconv.ParseUint(request.NetworkID, 10, 64)
	client := s.GetEVMClient(ctx, networkId)
	tx, err := client.Transact(tokenContractAddress, priKey, dataBytes, big.NewInt(0))
	if err != nil {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: failed to transact: %v", err)
	}
	txReceipt, err := s.GetEthereumClient(ctx, networkId).WaitMinedTxReceipt(ctx, common.HexToHash(tx))
	if err != nil {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: failed to wait tx receipt: %v", err)
	}

	if txReceipt.Status == types.ReceiptStatusFailed {
		return nil, fmt.Errorf("updateKnowledgeBaseInContractWithSignature error: tx exucute with status fail: %v", tx)
	}
	info.Status = models.KnowledgeBaseStatusMinted
	err = s.KnowledgeUsecase.UpdateKnowledgeBaseById(ctx, info.ID, map[string]interface{}{
		"status": info.Status,
	})
	if err != nil {
		return nil, err
	}
	return info, nil
}
