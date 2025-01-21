CONTRACT_ARTIFACT = {'_format': 'hh-sol-artifact-1',
                     'abi': [{'inputs': [{'internalType': 'bytes',
                                          'name': 'config',
                                          'type': 'bytes'}],
                              'stateMutability': 'nonpayable',
                              'type': 'constructor'},
                             {'inputs': [], 'name': 'IncorrectTensorType', 'type': 'error'},
                             {'inputs': [{'internalType': 'uint256[]',
                                          'name': 'x',
                                          'type': 'uint256[]'}],
                              'name': 'appendWeights',
                              'outputs': [{'internalType': 'bool', 'name': '', 'type': 'bool'}],
                              'stateMutability': 'nonpayable',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'epsilon',
                              'outputs': [{'internalType': 'uint256',
                                           'name': '',
                                           'type': 'uint256'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [{'components': [{'internalType': 'uint256[]',
                                                          'name': 'data',
                                                          'type': 'uint256[]'},
                                                         {'internalType': 'uint64[]',
                                                          'name': 'shapes',
                                                          'type': 'uint64[]'}],
                                          'internalType': 'struct Tensors.Tensor[]',
                                          'name': 'input',
                                          'type': 'tuple[]'}],
                              'name': 'forward',
                              'outputs': [{'components': [{'internalType': 'uint256[]',
                                                           'name': 'data',
                                                           'type': 'uint256[]'},
                                                          {'internalType': 'uint64[]',
                                                           'name': 'shapes',
                                                           'type': 'uint64[]'}],
                                           'internalType': 'struct Tensors.Tensor',
                                           'name': '',
                                           'type': 'tuple'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getBeta',
                              'outputs': [{'internalType': 'uint256[]',
                                           'name': '',
                                           'type': 'uint256[]'},
                                          {'internalType': 'uint64[]',
                                           'name': '',
                                           'type': 'uint64[]'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getGamma',
                              'outputs': [{'internalType': 'uint256[]',
                                           'name': '',
                                           'type': 'uint256[]'},
                                          {'internalType': 'uint64[]',
                                           'name': '',
                                           'type': 'uint64[]'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getMovingMean',
                              'outputs': [{'internalType': 'uint256[]',
                                           'name': '',
                                           'type': 'uint256[]'},
                                          {'internalType': 'uint64[]',
                                           'name': '',
                                           'type': 'uint64[]'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getMovingVariance',
                              'outputs': [{'internalType': 'uint256[]',
                                           'name': '',
                                           'type': 'uint256[]'},
                                          {'internalType': 'uint64[]',
                                           'name': '',
                                           'type': 'uint64[]'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getRemainingWeightCount',
                              'outputs': [{'internalType': 'uint256',
                                           'name': '',
                                           'type': 'uint256'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'getWeightCount',
                              'outputs': [{'internalType': 'uint256',
                                           'name': '',
                                           'type': 'uint256'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'inputUnits',
                              'outputs': [{'internalType': 'uint256',
                                           'name': '',
                                           'type': 'uint256'}],
                              'stateMutability': 'view',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'momentum',
                              'outputs': [{'internalType': 'uint256',
                                           'name': '',
                                           'type': 'uint256'}],
                              'stateMutability': 'view',
                              'type': 'function'}],
                     'bytecode': '0x60806040523462000030576200001e620000186200014d565b6200063a565b60405161156862000c53823961156890f35b600080fd5b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b038211176200006d57604052565b62000035565b906200008a6200008260405190565b92836200004b565b565b6001600160401b0381116200006d57602090601f01601f19160190565b60005b838110620000bd5750506000910152565b8181015183820152602001620000ac565b90929192620000e7620000e1826200008c565b62000073565b9381855260208501908284011162000030576200008a92620000a9565b9080601f83011215620000305781516200012192602001620000ce565b90565b90602082820312620000305781516001600160401b038111620000305762000121920162000104565b62000121620021bb80380380620001648162000073565b92833981019062000124565b90505190565b909160608284031262000030576200012162000193848462000170565b93620001a3816020860162000170565b9360400162000170565b90600019905b9181191691161790565b6200012162000121620001219290565b90620001e162000121620001e992620001bd565b8254620001ad565b9055565b620001219081565b620001219054620001ed565b6001600160401b0381116200006d5760208091020190565b9062000229620000e18362000201565b918252565b369037565b906200008a6200024e620002478462000219565b9362000201565b601f1901602084016200022e565b634e487b7160e01b600052601160045260246000fd5b818102929181159184041417156200028657565b6200025c565b9160001960089290920291821b911b620001b3565b9190620002b662000121620001e993620001bd565b9083546200028c565b6200008a9160005b91620002a1565b818110620002da575050565b80620002ea6000600193620002bf565b01620002ce565b906200030590600019906020036008021c90565b8154169055565b90918281106200031b57505050565b6200008a929062000333905b92600052602060002090565b9081019101620002ce565b906801000000000000000081116200006d57816200035e6200008a935490565b908281556200030c565b62000121916008021c81565b8151916001600160401b0383116200006d57620003a3620003276001926200039d86866200033e565b60200190565b92049160005b838110620003b75750505050565b6001906020620003c962000121865190565b9401938184015501620003a9565b906200008a9162000374565b62000121905b6001600160401b031690565b620001219060401c620003e9565b620001219060801c620003e9565b620001219060c01c620003e9565b906001906200044a6200043e62000434855490565b8084529260200190565b93600052602060002090565b6000926200051b575b6200045f565b50505090565b5490808310620004fa575b808310620004d9575b808310620004b8575b82106200048b575b8062000459565b82620004ae60019394620004a160209462000411565b6001600160401b03169052565b0191013862000484565b9192602081620004cf600193620004a18662000403565b019301916200047c565b9192602081620004f0600193620004a186620003f5565b0193019162000473565b919260208162000511600193620004a186620003e3565b019301916200046a565b6003830182111562000453579260016020620004a1620005796004948380808b54936200054d81620004a187620003e3565b016200055e81620004a186620003f5565b016200056f81620004a18562000403565b0192839162000411565b0194019201916200051b565b9062000121916200041f565b906200008a620005af92620005a560405190565b9384809262000585565b03836200004b565b620001219062000591565b634e487b7160e01b600052603260045260246000fd5b8054821015620005fd57620005f4600191600052602060002090565b91020190600090565b620005c2565b919082039182116200028657565b801562000286576000190190565b9062000121915462000368565b919082018092116200028657565b805160208201019060200190620006519162000176565b916200065f906000620001cd565b6200066c906001620001cd565b62000679906002620001cd565b6003620006876000620001f5565b620006929062000aed565b6200069e908262000aa5565b6005620006ac6000620001f5565b620006b79062000aed565b620006c3908262000aa5565b600790620006d26000620001f5565b620006dd9062000aed565b620006e9908362000aa5565b600992620006f86000620001f5565b620007039062000aed565b6200070f908562000aa5565b6200071b6004620001bd565b6200072890600d620001cd565b62000734600d620001f5565b6200073f9062000233565b6200074c90600e620003d7565b6200075a60018201620005b7565b620007659062000b5e565b90600e92600092620007788486620005d8565b620007849291620002a1565b6001016200079290620005b7565b6200079d9062000b5e565b6001958680968193620007b18389620005d8565b620007bd9291620002a1565b01620007c990620005b7565b620007d49062000b5e565b620007e1600287620005d8565b620007ed9291620002a1565b01620007f990620005b7565b620008049062000b5e565b90620008119084620005d8565b6200081d9291620002a1565b62000829600d620001f5565b6200083484620001bd565b6200083f9162000603565b925b6200084d575b50505050565b6200085881620001bd565b831115620008c857620008c183620008bb620008816200087a889787620005d8565b906200061f565b620002c7620008a66200089f620008988a620001bd565b8662000603565b88620005d8565b919092620008b583856200061f565b6200062c565b62000611565b9262000841565b62000847565b818110620008da575050565b80620008ea6000600193620002bf565b01620008ce565b9190918282106200090157505050565b6200008a92600890600490600301819004620009296004600387010494600052602060002090565b93840193019306026000811162000942575b50620008ce565b620009519060018303620002f1565b386200093b565b906801000000000000000081116200006d5781620009786200008a935490565b90828155620008f1565b916001600160401b0360089290920291821b911b620001b3565b90620009a6815190565b906001600160401b0382116200006d5762000327620009cb916200039d848662000958565b600482049160005b83811062000a47575060048302900360008111620009f15750505050565b92600093845b81811062000a0e5750505001553880808062000847565b909194602062000a3c60019262000a30620001218a516001600160401b031690565b90856008029062000982565b9601929101620009f7565b6000805b6004811062000a62575083820155600101620009d3565b9590602062000a8f60019262000a836200012186516001600160401b031690565b908a6008029062000982565b9201960162000a4b565b906200008a916200099c565b9060016200008a9262000ab88362000b5e565b81550162000a99565b620003e962000121620001219290565b9062000adb825190565b811015620005fd576020809102010190565b6200012162000b1262000b0b62000b056001620001bd565b62000233565b9262000ac1565b62000b2962000b226000620001bd565b8462000ad1565b906001600160401b03169052565b634e487b7160e01b600052601260045260246000fd5b811562000b58570490565b62000b37565b62000b8e62000b7b620001219262000b74600090565b5062000bc4565b62000b876003620001bd565b906200062c565b62000b9a6004620001bd565b9062000b4d565b6000198114620002865760010190565b620001219081906001600160401b031681565b60018062000bd281620001bd565b9262000bdf6000620001bd565b925b62000bec5750505090565b90919262000bfc62000121835190565b84101562000c4b5762000c3b62000c429162000c3462000c2e62000c21888762000ad1565b516001600160401b031690565b62000bb1565b9062000272565b9362000ba1565b91908162000be1565b926200045956fe6080604052600436101561001257600080fd5b60003560e01c806329cddf22146100c25780632aa40d86146100bd578063404601fd146100b85780635d37afd7146100b35780635f73ec8f146100ae578063645fae98146100a9578063a4604e78146100a4578063a7ba9fb11461009f578063b99ce9fc1461009a578063d1e841d8146100955763f945adab036100d25761042b565b610413565b6103f8565b6103dd565b6103b6565b61038f565b610377565b61034c565b610311565b6102e9565b61019c565b60009103126100d257565b600080fd5b906100f76100f06100e6845190565b8084529260200190565b9260200190565b9060005b8181106101085750505090565b90919261012561011e6001928651815260200190565b9460200190565b9291016100fb565b9061013c6100f06100e6845190565b9060005b81811061014d5750505090565b90919261016c61011e60019286516001600160401b0316815260200190565b929101610140565b604080825261019993919261018b918401906100d7565b91602081840391015261012d565b90565b346100d2576101ac3660046100c7565b6101b4610c06565b906101ca6101c160405190565b92839283610174565b0390f35b909182601f830112156100d2578135916001600160401b0383116100d25760200192602083028401116100d257565b906020828203126100d25781356001600160401b0381116100d25761022292016101ce565b9091565b906102356100f06100e6845190565b9060005b8181106102465750505090565b90919261025c61011e6001928651815260200190565b929101610239565b906102736100f06100e6845190565b9060005b8181106102845750505090565b9091926102a361011e60019286516001600160401b0316815260200190565b929101610277565b8051604080845261019993916020916102c79190840190610226565b920151906020818403910152610264565b6020808252610199929101906102ab565b346100d2576101ca6103056102ff3660046101fd565b90610a22565b604051918291826102d8565b346100d2576103213660046100c7565b6101b4610c3c565b610199916008021c81565b906101999154610329565b610199600080610334565b565b346100d25761035c3660046100c7565b6101ca61036761033f565b6040519182918290815260200190565b346100d2576103873660046100c7565b6101b4610c1c565b346100d25761039f3660046100c7565b6101ca6103676106ee565b61019960006001610334565b346100d2576103c63660046100c7565b6101ca6103676103aa565b61019960006002610334565b346100d2576103ed3660046100c7565b6101ca6103676103d1565b346100d2576104083660046100c7565b6101ca61036761066d565b346100d2576104233660046100c7565b6101b4610c2c565b346100d2576101ca6104476104413660046101fd565b90610afb565b60405191829182901515815260200190565b610199905b6001600160401b031690565b6101999060401c61045e565b6101999060801c61045e565b6101999060c01c61045e565b906001906104ac6104a06100e6855490565b93600052602060002090565b600092610566575b6104bf565b50505090565b5490808310610549575b80831061052c575b80831061050f575b82106104e6575b806104b9565b82610506600193946104f9602094610482565b6001600160401b03169052565b019101386104e0565b91926020816105236001936104f986610476565b019301916104d9565b91926020816105406001936104f98661046a565b019301916104d1565b919260208161055d6001936104f986610459565b019301916104c9565b600383018211156104b45792600160206104f96105b76004948380808b5493610592816104f987610459565b016105a0816104f98661046a565b016105ae816104f985610476565b01928391610482565b019401920191610566565b906101999161048e565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b0382111761060357604052565b6105cc565b9061034a6106229261061960405190565b938480926105c2565b03836105e2565b61019990610608565b6101996101996101999290565b634e487b7160e01b600052601160045260246000fd5b8181029291811591840414171561066857565b61063f565b61019961068261067d6004610629565b61146f565b61068c6004610632565b90610655565b6101999081565b6101999054610692565b634e487b7160e01b600052603260045260246000fd5b80548210156106dc576106d3600191600052602060002090565b91020190600090565b6106a3565b9190820391821161066857565b6106f8600b610699565b61070c610708610199600d610699565b9190565b0361071b576101996000610632565b61019961073c610736600e610730600b610699565b906106b9565b90610334565b610746600c610699565b906106e1565b9061034a61075960405190565b92836105e2565b610199604061074c565b610772610760565b906060825260606020830152565b61019961076a565b903590603e1936829003018212156100d2570190565b908210156106dc5760206101999202810190610788565b903590601e1936829003018212156100d257018035906001600160401b0382116100d2576020019160208202360383136100d257565b6001600160401b0381116106035760208091020190565b805b036100d257565b9050359061034a82610802565b9092919261082d610828826107eb565b61074c565b93818552602080860192028301928184116100d257915b8383106108515750505050565b6020809161085f848661080b565b815201920191610844565b9080601f830112156100d25781602061019993359101610818565b6001600160401b038116610804565b9050359061034a82610885565b909291926108b1610828826107eb565b93818552602080860192028301928184116100d257915b8383106108d55750505050565b602080916108e38486610894565b8152019201916108c8565b9080601f830112156100d257816020610199933591016108a1565b9190916040818403126100d257610920604061074c565b9281356001600160401b0381116100d2578161093d91840161086a565b845260208201356001600160401b0381116100d25761095c92016108ee565b6020830152565b610199903690610909565b9061098961097d6100e6845490565b92600052602060002090565b9060005b81811061099a5750505090565b9091926109be6109b76001926109af87610699565b815260200190565b9460010190565b92910161098d565b906101999161096e565b9061034a610622926109e160405190565b938480926109c6565b9061034a610a1260016109fb610760565b94610a0c610a08826109d0565b8752565b01610608565b6020840152565b610199906109ea565b90610a2b610780565b506000610a56610a51610a47610a4084610632565b858761079e565b60208101906107b5565b905090565b610a6261070883610632565b14610abe5761019992610a8692610a7b610a8193610632565b9161079e565b610963565b610a906002610699565b610a9a6001610699565b600991600791600591610ab8610ab280806003610a19565b95610a19565b95610e6c565b60405163035a803f60e01b8152600490fd5b90600019905b9181191691161790565b90610af0610199610af792610632565b8254610ad0565b9055565b610b05600b610699565b8092610b11600c610699565b9283610b1d6000610632565b93848114610bdc575b5050610b326001610632565b8514610bc1575b610b436002610632565b8514610ba6575b610b546003610632565b8514610b85575b505050610b7490610b6d83600b610ae0565b600c610ae0565b610b816107086004610632565b1490565b93610b9c9391610b7495610b97600990565b610ca2565b5090913880610b5b565b939092610bb7929184866007610ca2565b9193909290610b4a565b939092610bd2929184866005610ca2565b9193909290610b39565b9091955082610bf19493955086610b97600390565b91939092903880610b26565b610199906109d0565b600490610199610c166003610bfd565b92610629565b600690610199610c166005610bfd565b600890610199610c166007610bfd565b600a90610199610c166009610bfd565b91908110156106dc576020020190565b3561019981610802565b9160001960089290920291821b911b610ad6565b9190610c8b610199610af793610632565b908354610c66565b60001981146106685760010190565b939495909192610cb0600090565b50610cc061067d60018701610629565b955b84881080610d3a575b15610d1057610d03610d0a91610cfd610ced610ce88c8a8a610c4c565b610c5c565b610cf7838b6106b9565b90610c7a565b60010190565b9760010190565b96610cc2565b9695919450925090508414610d2457929190565b610d2f919350610c93565b916107086000610632565b50868110610ccb565b634e487b7160e01b600052602160045260246000fd5b601d1115610d6357565b610d43565b9061034a82610d59565b61019990610d68565b90610d88610828836107eb565b918252565b369037565b9061034a610da8610da284610d7b565b936107eb565b601f190160208401610d8d565b61045e6101996101999290565b610dd8610199610199926001600160401b031690565b60070b90565b90610de7825190565b8110156106dc576020809102010190565b60005b828110610e0757505050565b606082820152602001610dfb565b9061034a610e25610da284610d7b565b601f190160208401610df8565b60005b828110610e4157505050565b606082820152602001610e35565b9061034a610e5f610da284610d7b565b601f190160208401610e32565b949092939591610e7a610780565b50610e85600a610d72565b96610e906002610632565b91610e9a83610d92565b95610ea490610db5565b610ead90610dc2565b610eb76000610632565b610ec19088610dde565b90610ece919060070b9052565b610ed790610db5565b610ee090610dc2565b610eea6001610632565b610ef49087610dde565b90610f01919060070b9052565b610f0b6005610632565b95610f1587610e15565b966020890151610f256000610632565b610f2f908a610dde565b52610f3a6000610632565b610f449089610dde565b506020820151610f546001610632565b610f5e908a610dde565b52610f696001610632565b610f739089610dde565b506020830151610f83858a610dde565b52610f8e8489610dde565b506020850151610f9e6003610632565b610fa8908a610dde565b52610fb36003610632565b610fbd9089610dde565b506020860151610fcd6004610632565b610fd7908a610dde565b52610fe26004610632565b610fec9089610dde565b50610ff690610e4f565b97516110026000610632565b61100c908a610dde565b526110176000610632565b6110219089610dde565b505161102d6001610632565b6110379089610dde565b526110426001610632565b61104c9088610dde565b50516110588288610dde565b526110639086610dde565b505161106f6003610632565b6110799086610dde565b526110846003610632565b61108e9085610dde565b505161109a6004610632565b6110a49085610dde565b526110af6004610632565b6110b99084610dde565b506101999361135e565b906110d26100f06100e6845190565b9060005b8181106110e35750505090565b9091926110fc61011e600192865160070b815260200190565b9291016110d6565b9061019991610264565b9061112461111a835190565b8083529160200190565b90816111366020830284019460200190565b926000915b83831061114a57505050505090565b9091929394602061116d61116683856001950387528951611104565b9760200190565b930193019193929061113b565b9061019991610226565b9061119061111a835190565b90816111a26020830284019460200190565b926000915b8383106111b657505050505090565b909192939460206111d26111668385600195038752895161117a565b93019301919392906111a7565b92611213611221926101999694611206608088019260008901906001600160401b03169052565b86820360208801526110c3565b90848203604086015261110e565b916060818403910152611184565b9050519061034a82610802565b9092919261124c610828826107eb565b93818552602080860192028301928184116100d257915b8383106112705750505050565b6020809161127e848661122f565b815201920191611263565b9080601f830112156100d25781516101999260200161123c565b9050519061034a82610885565b909291926112c0610828826107eb565b93818552602080860192028301928184116100d257915b8383106112e45750505050565b602080916112f284866112a3565b8152019201916112d7565b9080601f830112156100d2578151610199926020016112b0565b9190916040818403126100d25780516001600160401b0381116100d25783611340918301611289565b9260208201516001600160401b0381116100d25761019992016112fd565b9161139761139c926113b19461138b61019997611379610780565b506040519586946020860194856111df565b908103825203826105e2565b6113ff565b60206113a6825190565b818301019101611317565b9061141f565b6001600160401b03811161060357602090601f01601f19160190565b90610d88610828836113b7565b3d156113fa576113ef3d6113d3565b903d6000602084013e565b606090565b6000809161140b606090565b5080519060200160575afa506101996113e0565b906101999061142c610780565b5061095c611438610760565b938452565b9190820180921161066857565b634e487b7160e01b600052601260045260246000fd5b811561146a570490565b61144a565b61149761148761019992611481600090565b506114bd565b6114916003610632565b9061143d565b6114a16004610632565b90611460565b610199610199610199926001600160401b031690565b6001806114c981610632565b926114d46000610632565b925b6114e05750505090565b9091926114ee610199835190565b84101561152c5761151e6115249161068c61151961150c8887610dde565b516001600160401b031690565b6114a7565b93610c93565b9190816114d6565b926104b956fea2646970667358221220a09397a8aad1f478337fae80fe2f599ec7f421e220fb513710647f62acae2e4664736f6c63430008130033',
                     'contractName': 'BatchNormalizationLayer',
                     'deployedBytecode': '0x6080604052600436101561001257600080fd5b60003560e01c806329cddf22146100c25780632aa40d86146100bd578063404601fd146100b85780635d37afd7146100b35780635f73ec8f146100ae578063645fae98146100a9578063a4604e78146100a4578063a7ba9fb11461009f578063b99ce9fc1461009a578063d1e841d8146100955763f945adab036100d25761042b565b610413565b6103f8565b6103dd565b6103b6565b61038f565b610377565b61034c565b610311565b6102e9565b61019c565b60009103126100d257565b600080fd5b906100f76100f06100e6845190565b8084529260200190565b9260200190565b9060005b8181106101085750505090565b90919261012561011e6001928651815260200190565b9460200190565b9291016100fb565b9061013c6100f06100e6845190565b9060005b81811061014d5750505090565b90919261016c61011e60019286516001600160401b0316815260200190565b929101610140565b604080825261019993919261018b918401906100d7565b91602081840391015261012d565b90565b346100d2576101ac3660046100c7565b6101b4610c06565b906101ca6101c160405190565b92839283610174565b0390f35b909182601f830112156100d2578135916001600160401b0383116100d25760200192602083028401116100d257565b906020828203126100d25781356001600160401b0381116100d25761022292016101ce565b9091565b906102356100f06100e6845190565b9060005b8181106102465750505090565b90919261025c61011e6001928651815260200190565b929101610239565b906102736100f06100e6845190565b9060005b8181106102845750505090565b9091926102a361011e60019286516001600160401b0316815260200190565b929101610277565b8051604080845261019993916020916102c79190840190610226565b920151906020818403910152610264565b6020808252610199929101906102ab565b346100d2576101ca6103056102ff3660046101fd565b90610a22565b604051918291826102d8565b346100d2576103213660046100c7565b6101b4610c3c565b610199916008021c81565b906101999154610329565b610199600080610334565b565b346100d25761035c3660046100c7565b6101ca61036761033f565b6040519182918290815260200190565b346100d2576103873660046100c7565b6101b4610c1c565b346100d25761039f3660046100c7565b6101ca6103676106ee565b61019960006001610334565b346100d2576103c63660046100c7565b6101ca6103676103aa565b61019960006002610334565b346100d2576103ed3660046100c7565b6101ca6103676103d1565b346100d2576104083660046100c7565b6101ca61036761066d565b346100d2576104233660046100c7565b6101b4610c2c565b346100d2576101ca6104476104413660046101fd565b90610afb565b60405191829182901515815260200190565b610199905b6001600160401b031690565b6101999060401c61045e565b6101999060801c61045e565b6101999060c01c61045e565b906001906104ac6104a06100e6855490565b93600052602060002090565b600092610566575b6104bf565b50505090565b5490808310610549575b80831061052c575b80831061050f575b82106104e6575b806104b9565b82610506600193946104f9602094610482565b6001600160401b03169052565b019101386104e0565b91926020816105236001936104f986610476565b019301916104d9565b91926020816105406001936104f98661046a565b019301916104d1565b919260208161055d6001936104f986610459565b019301916104c9565b600383018211156104b45792600160206104f96105b76004948380808b5493610592816104f987610459565b016105a0816104f98661046a565b016105ae816104f985610476565b01928391610482565b019401920191610566565b906101999161048e565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b0382111761060357604052565b6105cc565b9061034a6106229261061960405190565b938480926105c2565b03836105e2565b61019990610608565b6101996101996101999290565b634e487b7160e01b600052601160045260246000fd5b8181029291811591840414171561066857565b61063f565b61019961068261067d6004610629565b61146f565b61068c6004610632565b90610655565b6101999081565b6101999054610692565b634e487b7160e01b600052603260045260246000fd5b80548210156106dc576106d3600191600052602060002090565b91020190600090565b6106a3565b9190820391821161066857565b6106f8600b610699565b61070c610708610199600d610699565b9190565b0361071b576101996000610632565b61019961073c610736600e610730600b610699565b906106b9565b90610334565b610746600c610699565b906106e1565b9061034a61075960405190565b92836105e2565b610199604061074c565b610772610760565b906060825260606020830152565b61019961076a565b903590603e1936829003018212156100d2570190565b908210156106dc5760206101999202810190610788565b903590601e1936829003018212156100d257018035906001600160401b0382116100d2576020019160208202360383136100d257565b6001600160401b0381116106035760208091020190565b805b036100d257565b9050359061034a82610802565b9092919261082d610828826107eb565b61074c565b93818552602080860192028301928184116100d257915b8383106108515750505050565b6020809161085f848661080b565b815201920191610844565b9080601f830112156100d25781602061019993359101610818565b6001600160401b038116610804565b9050359061034a82610885565b909291926108b1610828826107eb565b93818552602080860192028301928184116100d257915b8383106108d55750505050565b602080916108e38486610894565b8152019201916108c8565b9080601f830112156100d257816020610199933591016108a1565b9190916040818403126100d257610920604061074c565b9281356001600160401b0381116100d2578161093d91840161086a565b845260208201356001600160401b0381116100d25761095c92016108ee565b6020830152565b610199903690610909565b9061098961097d6100e6845490565b92600052602060002090565b9060005b81811061099a5750505090565b9091926109be6109b76001926109af87610699565b815260200190565b9460010190565b92910161098d565b906101999161096e565b9061034a610622926109e160405190565b938480926109c6565b9061034a610a1260016109fb610760565b94610a0c610a08826109d0565b8752565b01610608565b6020840152565b610199906109ea565b90610a2b610780565b506000610a56610a51610a47610a4084610632565b858761079e565b60208101906107b5565b905090565b610a6261070883610632565b14610abe5761019992610a8692610a7b610a8193610632565b9161079e565b610963565b610a906002610699565b610a9a6001610699565b600991600791600591610ab8610ab280806003610a19565b95610a19565b95610e6c565b60405163035a803f60e01b8152600490fd5b90600019905b9181191691161790565b90610af0610199610af792610632565b8254610ad0565b9055565b610b05600b610699565b8092610b11600c610699565b9283610b1d6000610632565b93848114610bdc575b5050610b326001610632565b8514610bc1575b610b436002610632565b8514610ba6575b610b546003610632565b8514610b85575b505050610b7490610b6d83600b610ae0565b600c610ae0565b610b816107086004610632565b1490565b93610b9c9391610b7495610b97600990565b610ca2565b5090913880610b5b565b939092610bb7929184866007610ca2565b9193909290610b4a565b939092610bd2929184866005610ca2565b9193909290610b39565b9091955082610bf19493955086610b97600390565b91939092903880610b26565b610199906109d0565b600490610199610c166003610bfd565b92610629565b600690610199610c166005610bfd565b600890610199610c166007610bfd565b600a90610199610c166009610bfd565b91908110156106dc576020020190565b3561019981610802565b9160001960089290920291821b911b610ad6565b9190610c8b610199610af793610632565b908354610c66565b60001981146106685760010190565b939495909192610cb0600090565b50610cc061067d60018701610629565b955b84881080610d3a575b15610d1057610d03610d0a91610cfd610ced610ce88c8a8a610c4c565b610c5c565b610cf7838b6106b9565b90610c7a565b60010190565b9760010190565b96610cc2565b9695919450925090508414610d2457929190565b610d2f919350610c93565b916107086000610632565b50868110610ccb565b634e487b7160e01b600052602160045260246000fd5b601d1115610d6357565b610d43565b9061034a82610d59565b61019990610d68565b90610d88610828836107eb565b918252565b369037565b9061034a610da8610da284610d7b565b936107eb565b601f190160208401610d8d565b61045e6101996101999290565b610dd8610199610199926001600160401b031690565b60070b90565b90610de7825190565b8110156106dc576020809102010190565b60005b828110610e0757505050565b606082820152602001610dfb565b9061034a610e25610da284610d7b565b601f190160208401610df8565b60005b828110610e4157505050565b606082820152602001610e35565b9061034a610e5f610da284610d7b565b601f190160208401610e32565b949092939591610e7a610780565b50610e85600a610d72565b96610e906002610632565b91610e9a83610d92565b95610ea490610db5565b610ead90610dc2565b610eb76000610632565b610ec19088610dde565b90610ece919060070b9052565b610ed790610db5565b610ee090610dc2565b610eea6001610632565b610ef49087610dde565b90610f01919060070b9052565b610f0b6005610632565b95610f1587610e15565b966020890151610f256000610632565b610f2f908a610dde565b52610f3a6000610632565b610f449089610dde565b506020820151610f546001610632565b610f5e908a610dde565b52610f696001610632565b610f739089610dde565b506020830151610f83858a610dde565b52610f8e8489610dde565b506020850151610f9e6003610632565b610fa8908a610dde565b52610fb36003610632565b610fbd9089610dde565b506020860151610fcd6004610632565b610fd7908a610dde565b52610fe26004610632565b610fec9089610dde565b50610ff690610e4f565b97516110026000610632565b61100c908a610dde565b526110176000610632565b6110219089610dde565b505161102d6001610632565b6110379089610dde565b526110426001610632565b61104c9088610dde565b50516110588288610dde565b526110639086610dde565b505161106f6003610632565b6110799086610dde565b526110846003610632565b61108e9085610dde565b505161109a6004610632565b6110a49085610dde565b526110af6004610632565b6110b99084610dde565b506101999361135e565b906110d26100f06100e6845190565b9060005b8181106110e35750505090565b9091926110fc61011e600192865160070b815260200190565b9291016110d6565b9061019991610264565b9061112461111a835190565b8083529160200190565b90816111366020830284019460200190565b926000915b83831061114a57505050505090565b9091929394602061116d61116683856001950387528951611104565b9760200190565b930193019193929061113b565b9061019991610226565b9061119061111a835190565b90816111a26020830284019460200190565b926000915b8383106111b657505050505090565b909192939460206111d26111668385600195038752895161117a565b93019301919392906111a7565b92611213611221926101999694611206608088019260008901906001600160401b03169052565b86820360208801526110c3565b90848203604086015261110e565b916060818403910152611184565b9050519061034a82610802565b9092919261124c610828826107eb565b93818552602080860192028301928184116100d257915b8383106112705750505050565b6020809161127e848661122f565b815201920191611263565b9080601f830112156100d25781516101999260200161123c565b9050519061034a82610885565b909291926112c0610828826107eb565b93818552602080860192028301928184116100d257915b8383106112e45750505050565b602080916112f284866112a3565b8152019201916112d7565b9080601f830112156100d2578151610199926020016112b0565b9190916040818403126100d25780516001600160401b0381116100d25783611340918301611289565b9260208201516001600160401b0381116100d25761019992016112fd565b9161139761139c926113b19461138b61019997611379610780565b506040519586946020860194856111df565b908103825203826105e2565b6113ff565b60206113a6825190565b818301019101611317565b9061141f565b6001600160401b03811161060357602090601f01601f19160190565b90610d88610828836113b7565b3d156113fa576113ef3d6113d3565b903d6000602084013e565b606090565b6000809161140b606090565b5080519060200160575afa506101996113e0565b906101999061142c610780565b5061095c611438610760565b938452565b9190820180921161066857565b634e487b7160e01b600052601260045260246000fd5b811561146a570490565b61144a565b61149761148761019992611481600090565b506114bd565b6114916003610632565b9061143d565b6114a16004610632565b90611460565b610199610199610199926001600160401b031690565b6001806114c981610632565b926114d46000610632565b925b6114e05750505090565b9091926114ee610199835190565b84101561152c5761151e6115249161068c61151961150c8887610dde565b516001600160401b031690565b6114a7565b93610c93565b9190816114d6565b926104b956fea2646970667358221220a09397a8aad1f478337fae80fe2f599ec7f421e220fb513710647f62acae2e4664736f6c63430008130033',
                     'deployedLinkReferences': {},
                     'linkReferences': {},
                     'sourceName': 'contracts/lib/layers-new/BatchNormalizationLayer.sol'}
