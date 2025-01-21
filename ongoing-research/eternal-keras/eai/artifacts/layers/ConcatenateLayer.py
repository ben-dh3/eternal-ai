CONTRACT_ARTIFACT = {'_format': 'hh-sol-artifact-1',
                     'abi': [{'inputs': [{'internalType': 'bytes',
                                          'name': 'config',
                                          'type': 'bytes'}],
                              'stateMutability': 'nonpayable',
                              'type': 'constructor'},
                             {'inputs': [],
                              'name': 'IncorrectTensorDim',
                              'type': 'error'},
                             {'inputs': [],
                              'name': 'IncorrectTensorType',
                              'type': 'error'},
                             {'inputs': [{'internalType': 'uint256[]',
                                          'name': 'x',
                                          'type': 'uint256[]'}],
                              'name': 'appendWeights',
                              'outputs': [{'internalType': 'bool',
                                           'name': '',
                                           'type': 'bool'}],
                              'stateMutability': 'nonpayable',
                              'type': 'function'},
                             {'inputs': [],
                              'name': 'axis',
                              'outputs': [{'internalType': 'int8',
                                           'name': '',
                                           'type': 'int8'}],
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
                              'type': 'function'}],
                     'bytecode': '0x60806040523462000030576200001e620000186200014d565b620001ea565b604051610ec9620002138239610ec990f35b600080fd5b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b038211176200006d57604052565b62000035565b906200008a6200008260405190565b92836200004b565b565b6001600160401b0381116200006d57602090601f01601f19160190565b60005b838110620000bd5750506000910152565b8181015183820152602001620000ac565b90929192620000e7620000e1826200008c565b62000073565b9381855260208501908284011162000030576200008a92620000a9565b9080601f83011215620000305781516200012192602001620000ce565b90565b90602082820312620000305781516001600160401b038111620000305762000121920162000104565b62000121620010dc80380380620001648162000073565b92833981019062000124565b6200017b8160000b90565b036200003057565b905051906200008a8262000170565b906020828203126200003057620001219162000183565b620001bc62000121620001219260000b90565b60000b90565b90620001d662000121620001e692620001a9565b825460ff191660ff919091161790565b9055565b6200020a6200008a916020620001fe825190565b81830101910162000192565b6000620001c256fe6080604052600436101561001257600080fd5b60003560e01c80631f0491c81461005d5780632aa40d8614610058578063645fae9814610053578063b99ce9fc146100535763f945adab0361006d57610256565b61022b565b610203565b61009c565b600091031261006d57565b600080fd5b610081916008021c5b60000b90565b90565b906100819154610072565b610081600080610084565b565b3461006d576100ac366004610062565b6100cc6100b761008f565b6040519182918260009190910b815260200190565b0390f35b909182601f8301121561006d578135916001600160401b03831161006d57602001926020830284011161006d57565b9060208282031261006d5781356001600160401b03811161006d5761012492016100d0565b9091565b90610148610141610137845190565b8084529260200190565b9260200190565b9060005b8181106101595750505090565b90919261017661016f6001928651815260200190565b9460200190565b92910161014c565b9061018d610141610137845190565b9060005b81811061019e5750505090565b9091926101bd61016f60019286516001600160401b0316815260200190565b929101610191565b8051604080845261008193916020916101e19190840190610128565b92015190602081840391015261017e565b6020808252610081929101906101c5565b3461006d576100cc61021f6102193660046100ff565b90610619565b604051918291826101f2565b3461006d5761023b366004610062565b6100cc610246610291565b6040519182918290815260200190565b3461006d576100cc61027261026c3660046100ff565b906108b9565b60405191829182901515815260200190565b6100816100816100819290565b6100816000610284565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b038211176102d257604052565b61029b565b9061009a6102e460405190565b92836102b1565b61008160406102d7565b6102fd6102eb565b906060825260606020830152565b6100816102f5565b634e487b7160e01b600052603260045260246000fd5b903590603e19368290030182121561006d570190565b908210156103565760206100819202810190610329565b610313565b903590601e19368290030182121561006d57018035906001600160401b03821161006d5760200191602082023603831361006d57565b6100819061007b565b6100819054610391565b61007b6100816100819290565b6100816100816100819260000b90565b6103d16100816100819260000b90565b60ff1690565b634e487b7160e01b600052601160045260246000fd5b919082039182116103fa57565b6103d7565b6103d16100816100819290565b60001981146103fa5760010190565b6001600160401b0381116102d25760208091020190565b6001600160401b0381165b0361006d57565b9050359061009a82610432565b909291926104666104618261041b565b6102d7565b938185526020808601920283019281841161006d57915b83831061048a5750505050565b602080916104988486610444565b81520192019161047d565b610081913691610451565b8061043d565b9050359061009a826104ae565b909291926104d16104618261041b565b938185526020808601920283019281841161006d57915b8383106104f55750505050565b6020809161050384866104b4565b8152019201916104e8565b9080601f8301121561006d57816020610081933591016104c1565b9080601f8301121561006d5781602061008193359101610451565b91909160408184031261006d5761055b60406102d7565b9281356001600160401b03811161006d578161057891840161050e565b845260208201356001600160401b03811161006d576105979201610529565b6020830152565b9291906105ad6104618261041b565b938185526020808601920281019183831161006d5781905b8382106105d3575050505050565b81356001600160401b03811161006d576020916105f38784938701610544565b8152019101906105c5565b61008191369161059e565b6100816100816100819260ff1690565b919061062361030b565b5060009061064f61064a61064061063985610284565b848861033f565b602081019061035b565b905090565b61065f61065b84610284565b9190565b146107c95761066d8261039a565b61068161067a84196103a4565b9160000b90565b0361076f576106ba6106b56106a561064a61064061069e87610284565b868a61033f565b6106af6001610284565b906103ed565b6103ff565b915b600190816106c981610284565b905b6106f0575b5050506106e46106ea9161008194956105fe565b91610609565b906109d8565b8381101561076a57610744610740868961073a8861073461072c6106408961072461064061071d8e610284565b878a61033f565b95909761033f565b9290946104a3565b926104a3565b906107f5565b1590565b610757576107519061040c565b826106cb565b6040515b6378ceb26560e11b8152600490fd5b6106d0565b6107788261039a565b6107a561079f61008161079a61064a61064061079389610284565b888c61033f565b610284565b916103b1565b126107b25760405161075b565b6107c36107be8361039a565b6103c1565b916106bc565b60405163035a803f60e01b8152600490fd5b906107e4825190565b811015610356576020809102010190565b9190825161080761065b610081845190565b036108b15782519260009261081b84610284565b855b8110156108a65761082d82610609565b811461089a5761084d61084082856107db565b516001600160401b031690565b61087961086c61086061084085896107db565b6001600160401b031690565b916001600160401b031690565b036108915761088a61081d9161040c565b905061081b565b50505050905090565b61088a61081d9161040c565b505050505050600190565b505050600090565b50506108c3600090565b50600190565b634e487b7160e01b600052602160045260246000fd5b601d11156108e957565b6108c9565b9061009a826108df565b610081906108ee565b9061090e6104618361041b565b918252565b369037565b9061009a61092e61092884610901565b9361041b565b601f190160208401610913565b6108606100816100819290565b61095e610081610081926001600160401b031690565b60070b90565b60005b82811061097357505050565b606082820152602001610967565b9061009a61099161092884610901565b601f190160208401610964565b60005b8281106109ad57505050565b6060828201526020016109a1565b9061009a6109cb61092884610901565b601f19016020840161099e565b9190916109e361030b565b506109ee600e6108f8565b92600190610a14610a0f610a09610a0485610284565b610918565b9261093b565b610948565b94610a35600096610a2d610a2789610284565b856107db565b9060070b9052565b610a45610a40855190565b610981565b928080610a5189610284565b905b610ad4575b5050610a6a610a65865190565b6109bb565b9481610a7589610284565b905b610a8a575b505050610081949550610db4565b610a95610081835190565b811015610acf578089610aab610ac993856107db565b510151610ab8828a6107db565b52610ac381896107db565b5061040c565b82610a77565b610a7c565b610adf610081885190565b811015610b1457806020610af6610b0e938a6107db565b510151610b0382896107db565b52610ac381886107db565b81610a53565b610a58565b90610b28610141610137845190565b9060005b818110610b395750505090565b909192610b5261016f600192865160070b815260200190565b929101610b2c565b906100819161017e565b90610b7a610b70835190565b8083529160200190565b9081610b8c6020830284019460200190565b926000915b838310610ba057505050505090565b90919293946020610bc3610bbc83856001950387528951610b5a565b9760200190565b9301930191939290610b91565b9061008191610128565b90610be6610b70835190565b9081610bf86020830284019460200190565b926000915b838310610c0c57505050505090565b90919293946020610c28610bbc83856001950387528951610bd0565b9301930191939290610bfd565b92610c69610c77926100819694610c5c608088019260008901906001600160401b03169052565b8682036020880152610b19565b908482036040860152610b64565b916060818403910152610bda565b9050519061009a826104ae565b90929192610ca26104618261041b565b938185526020808601920283019281841161006d57915b838310610cc65750505050565b60208091610cd48486610c85565b815201920191610cb9565b9080601f8301121561006d57815161008192602001610c92565b9050519061009a82610432565b90929192610d166104618261041b565b938185526020808601920283019281841161006d57915b838310610d3a5750505050565b60208091610d488486610cf9565b815201920191610d2d565b9080601f8301121561006d57815161008192602001610d06565b91909160408184031261006d5780516001600160401b03811161006d5783610d96918301610cdf565b9260208201516001600160401b03811161006d576100819201610d53565b91610ded610df292610e0794610de161008197610dcf61030b565b50604051958694602086019485610c35565b908103825203826102b1565b610e55565b6020610dfc825190565b818301019101610d6d565b90610e75565b6001600160401b0381116102d257602090601f01601f19160190565b9061090e61046183610e0d565b3d15610e5057610e453d610e29565b903d6000602084013e565b606090565b60008091610e61606090565b5080519060200160575afa50610081610e36565b9061008190610e8261030b565b50610597610e8e6102eb565b93845256fea2646970667358221220efb7c525d0e72f4dda5e43243f5cb3caff8286d9528012cd139fd2150fdc025064736f6c63430008130033',
                     'contractName': 'ConcatenateLayer',
                     'deployedBytecode': '0x6080604052600436101561001257600080fd5b60003560e01c80631f0491c81461005d5780632aa40d8614610058578063645fae9814610053578063b99ce9fc146100535763f945adab0361006d57610256565b61022b565b610203565b61009c565b600091031261006d57565b600080fd5b610081916008021c5b60000b90565b90565b906100819154610072565b610081600080610084565b565b3461006d576100ac366004610062565b6100cc6100b761008f565b6040519182918260009190910b815260200190565b0390f35b909182601f8301121561006d578135916001600160401b03831161006d57602001926020830284011161006d57565b9060208282031261006d5781356001600160401b03811161006d5761012492016100d0565b9091565b90610148610141610137845190565b8084529260200190565b9260200190565b9060005b8181106101595750505090565b90919261017661016f6001928651815260200190565b9460200190565b92910161014c565b9061018d610141610137845190565b9060005b81811061019e5750505090565b9091926101bd61016f60019286516001600160401b0316815260200190565b929101610191565b8051604080845261008193916020916101e19190840190610128565b92015190602081840391015261017e565b6020808252610081929101906101c5565b3461006d576100cc61021f6102193660046100ff565b90610619565b604051918291826101f2565b3461006d5761023b366004610062565b6100cc610246610291565b6040519182918290815260200190565b3461006d576100cc61027261026c3660046100ff565b906108b9565b60405191829182901515815260200190565b6100816100816100819290565b6100816000610284565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b038211176102d257604052565b61029b565b9061009a6102e460405190565b92836102b1565b61008160406102d7565b6102fd6102eb565b906060825260606020830152565b6100816102f5565b634e487b7160e01b600052603260045260246000fd5b903590603e19368290030182121561006d570190565b908210156103565760206100819202810190610329565b610313565b903590601e19368290030182121561006d57018035906001600160401b03821161006d5760200191602082023603831361006d57565b6100819061007b565b6100819054610391565b61007b6100816100819290565b6100816100816100819260000b90565b6103d16100816100819260000b90565b60ff1690565b634e487b7160e01b600052601160045260246000fd5b919082039182116103fa57565b6103d7565b6103d16100816100819290565b60001981146103fa5760010190565b6001600160401b0381116102d25760208091020190565b6001600160401b0381165b0361006d57565b9050359061009a82610432565b909291926104666104618261041b565b6102d7565b938185526020808601920283019281841161006d57915b83831061048a5750505050565b602080916104988486610444565b81520192019161047d565b610081913691610451565b8061043d565b9050359061009a826104ae565b909291926104d16104618261041b565b938185526020808601920283019281841161006d57915b8383106104f55750505050565b6020809161050384866104b4565b8152019201916104e8565b9080601f8301121561006d57816020610081933591016104c1565b9080601f8301121561006d5781602061008193359101610451565b91909160408184031261006d5761055b60406102d7565b9281356001600160401b03811161006d578161057891840161050e565b845260208201356001600160401b03811161006d576105979201610529565b6020830152565b9291906105ad6104618261041b565b938185526020808601920281019183831161006d5781905b8382106105d3575050505050565b81356001600160401b03811161006d576020916105f38784938701610544565b8152019101906105c5565b61008191369161059e565b6100816100816100819260ff1690565b919061062361030b565b5060009061064f61064a61064061063985610284565b848861033f565b602081019061035b565b905090565b61065f61065b84610284565b9190565b146107c95761066d8261039a565b61068161067a84196103a4565b9160000b90565b0361076f576106ba6106b56106a561064a61064061069e87610284565b868a61033f565b6106af6001610284565b906103ed565b6103ff565b915b600190816106c981610284565b905b6106f0575b5050506106e46106ea9161008194956105fe565b91610609565b906109d8565b8381101561076a57610744610740868961073a8861073461072c6106408961072461064061071d8e610284565b878a61033f565b95909761033f565b9290946104a3565b926104a3565b906107f5565b1590565b610757576107519061040c565b826106cb565b6040515b6378ceb26560e11b8152600490fd5b6106d0565b6107788261039a565b6107a561079f61008161079a61064a61064061079389610284565b888c61033f565b610284565b916103b1565b126107b25760405161075b565b6107c36107be8361039a565b6103c1565b916106bc565b60405163035a803f60e01b8152600490fd5b906107e4825190565b811015610356576020809102010190565b9190825161080761065b610081845190565b036108b15782519260009261081b84610284565b855b8110156108a65761082d82610609565b811461089a5761084d61084082856107db565b516001600160401b031690565b61087961086c61086061084085896107db565b6001600160401b031690565b916001600160401b031690565b036108915761088a61081d9161040c565b905061081b565b50505050905090565b61088a61081d9161040c565b505050505050600190565b505050600090565b50506108c3600090565b50600190565b634e487b7160e01b600052602160045260246000fd5b601d11156108e957565b6108c9565b9061009a826108df565b610081906108ee565b9061090e6104618361041b565b918252565b369037565b9061009a61092e61092884610901565b9361041b565b601f190160208401610913565b6108606100816100819290565b61095e610081610081926001600160401b031690565b60070b90565b60005b82811061097357505050565b606082820152602001610967565b9061009a61099161092884610901565b601f190160208401610964565b60005b8281106109ad57505050565b6060828201526020016109a1565b9061009a6109cb61092884610901565b601f19016020840161099e565b9190916109e361030b565b506109ee600e6108f8565b92600190610a14610a0f610a09610a0485610284565b610918565b9261093b565b610948565b94610a35600096610a2d610a2789610284565b856107db565b9060070b9052565b610a45610a40855190565b610981565b928080610a5189610284565b905b610ad4575b5050610a6a610a65865190565b6109bb565b9481610a7589610284565b905b610a8a575b505050610081949550610db4565b610a95610081835190565b811015610acf578089610aab610ac993856107db565b510151610ab8828a6107db565b52610ac381896107db565b5061040c565b82610a77565b610a7c565b610adf610081885190565b811015610b1457806020610af6610b0e938a6107db565b510151610b0382896107db565b52610ac381886107db565b81610a53565b610a58565b90610b28610141610137845190565b9060005b818110610b395750505090565b909192610b5261016f600192865160070b815260200190565b929101610b2c565b906100819161017e565b90610b7a610b70835190565b8083529160200190565b9081610b8c6020830284019460200190565b926000915b838310610ba057505050505090565b90919293946020610bc3610bbc83856001950387528951610b5a565b9760200190565b9301930191939290610b91565b9061008191610128565b90610be6610b70835190565b9081610bf86020830284019460200190565b926000915b838310610c0c57505050505090565b90919293946020610c28610bbc83856001950387528951610bd0565b9301930191939290610bfd565b92610c69610c77926100819694610c5c608088019260008901906001600160401b03169052565b8682036020880152610b19565b908482036040860152610b64565b916060818403910152610bda565b9050519061009a826104ae565b90929192610ca26104618261041b565b938185526020808601920283019281841161006d57915b838310610cc65750505050565b60208091610cd48486610c85565b815201920191610cb9565b9080601f8301121561006d57815161008192602001610c92565b9050519061009a82610432565b90929192610d166104618261041b565b938185526020808601920283019281841161006d57915b838310610d3a5750505050565b60208091610d488486610cf9565b815201920191610d2d565b9080601f8301121561006d57815161008192602001610d06565b91909160408184031261006d5780516001600160401b03811161006d5783610d96918301610cdf565b9260208201516001600160401b03811161006d576100819201610d53565b91610ded610df292610e0794610de161008197610dcf61030b565b50604051958694602086019485610c35565b908103825203826102b1565b610e55565b6020610dfc825190565b818301019101610d6d565b90610e75565b6001600160401b0381116102d257602090601f01601f19160190565b9061090e61046183610e0d565b3d15610e5057610e453d610e29565b903d6000602084013e565b606090565b60008091610e61606090565b5080519060200160575afa50610081610e36565b9061008190610e8261030b565b50610597610e8e6102eb565b93845256fea2646970667358221220efb7c525d0e72f4dda5e43243f5cb3caff8286d9528012cd139fd2150fdc025064736f6c63430008130033',
                     'deployedLinkReferences': {},
                     'linkReferences': {},
                     'sourceName': 'contracts/lib/layers-new/ConcatenateLayer.sol'}
