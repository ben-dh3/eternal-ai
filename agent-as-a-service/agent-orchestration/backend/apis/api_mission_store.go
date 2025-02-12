package apis

import (
	"net/http"
	"strconv"

	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/errs"
	"github.com/eternalai-org/eternal-ai/agent-as-a-service/agent-orchestration/backend/serializers"
	"github.com/gin-gonic/gin"
)

func (s *Server) UploadMissionStore(c *gin.Context) {
	ctx := s.requestContext(c)
	var req serializers.MissionStoreReq
	if err := c.ShouldBindJSON(&req); err != nil {
		ctxJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	err := s.nls.UploadMisstionStore(ctx, &req)
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: true})
}

func (s *Server) RateMissionStore(c *gin.Context) {
	ctx := s.requestContext(c)
	var req serializers.MissionStoreRatingReq
	if err := c.ShouldBindJSON(&req); err != nil {
		ctxJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	err := s.nls.RatingMisstionStore(ctx, &req)
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: true})
}

func (s *Server) GetListMissionStore(c *gin.Context) {
	ctx := s.requestContext(c)
	page, limit := s.pagingFromContext(c)
	search := s.stringFromContextQuery(c, "search")
	res, count, err := s.nls.GetListMisstionStore(ctx, search, page, limit)
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: serializers.NewMissionStoreRespArray(res), Count: &count})
}

func (s *Server) GetMissionStoreDetail(c *gin.Context) {
	ctx := s.requestContext(c)
	idStr := s.stringFromContextParam(c, "id")
	id, _ := strconv.ParseUint(idStr, 10, 64)
	res, err := s.nls.GetMisstionStoreDetail(ctx, uint(id))
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: serializers.NewMissionStoreResp(res)})
}

func (s *Server) GetMissionStoreRating(c *gin.Context) {
	ctx := s.requestContext(c)
	missionStoreIDstr := s.stringFromContextParam(c, "id")
	missionStoreID, _ := strconv.ParseUint(missionStoreIDstr, 10, 64)
	page, limit := s.pagingFromContext(c)
	res, count, err := s.nls.GetMissionStoreRating(ctx, uint(missionStoreID), page, limit)
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: serializers.NewMissionStoreRatingRespArray(res), Count: &count})

}

func (s *Server) ClaimFeeMissionStore(c *gin.Context) {
	ctx := s.requestContext(c)
	s.nls.ClaimFeeMisstionStore(ctx)
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: true})
}

func (s *Server) GetMissionStoreHistory(c *gin.Context) {
	ctx := s.requestContext(c)
	missionStoreIDstr := s.stringFromContextParam(c, "id")
	missionStoreID, _ := strconv.ParseUint(missionStoreIDstr, 10, 64)
	page, limit := s.pagingFromContext(c)
	res, count, err := s.nls.GetMissionStoreHistory(ctx, uint(missionStoreID), page, limit)
	if err != nil {
		ctxAbortWithStatusJSON(c, http.StatusBadRequest, &serializers.Resp{Error: errs.NewError(err)})
		return
	}
	ctxJSON(c, http.StatusOK, &serializers.Resp{Result: serializers.NewMissionStoreHistoryRespArray(res), Count: &count})

}
