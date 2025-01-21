CONTRACT_ARTIFACT = {'_format': 'hh-sol-artifact-1',
                     'abi': [{'inputs': [{'internalType': 'bytes',
                                          'name': 'config',
                                          'type': 'bytes'}],
                              'stateMutability': 'nonpayable',
                              'type': 'constructor'},
                             {'inputs': [],
                              'name': 'IncorrectTensorType',
                              'type': 'error'},
                             {'inputs': [],
                              'name': 'InvalidActivationFunction',
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
                     'bytecode': '0x60806040523462000027576200001462000144565b50604051610d35620001688239610d3590f35b600080fd5b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b038211176200006457604052565b6200002c565b90620000816200007960405190565b928362000042565b565b6001600160401b0381116200006457602090601f01601f19160190565b60005b838110620000b45750506000910152565b8181015183820152602001620000a3565b90929192620000de620000d88262000083565b6200006a565b9381855260208501908284011162000027576200008192620000a0565b9080601f83011215620000275781516200011892602001620000c5565b90565b90602082820312620000275781516001600160401b0381116200002757620001189201620000fb565b6200011862000e9d803803806200015b816200006a565b9283398101906200011b56fe6080604052600436101561001257600080fd5b60003560e01c80632aa40d861461004d578063645fae9814610048578063b99ce9fc146100485763f945adab03610081576101f1565b6101c6565b61018d565b909182601f83011215610081578135916001600160401b03831161008157602001926020830284011161008157565b600080fd5b906020828203126100815781356001600160401b038111610081576100ab9201610052565b9091565b906100cf6100c86100be845190565b8084529260200190565b9260200190565b9060005b8181106100e05750505090565b9091926100fd6100f66001928651815260200190565b9460200190565b9291016100d3565b906101146100c86100be845190565b9060005b8181106101255750505090565b9091926101446100f660019286516001600160401b0316815260200190565b929101610118565b80516040808452610179939160209161016891908401906100af565b920151906020818403910152610105565b90565b60208082526101799291019061014c565b34610081576101b56101a96101a3366004610086565b906104af565b6040519182918261017c565b0390f35b600091031261008157565b565b34610081576101d63660046101b9565b6101b56101e161022c565b6040519182918290815260200190565b34610081576101b561020d610207366004610086565b90610535565b60405191829182901515815260200190565b6101796101796101799290565b610179600061021f565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b0382111761026d57604052565b610236565b906101c461027f60405190565b928361024c565b6101796040610272565b610298610286565b906060825260606020830152565b610179610290565b634e487b7160e01b600052603260045260246000fd5b903590603e193682900301821215610081570190565b908210156102f157602061017992028101906102c4565b6102ae565b903590601e19368290030182121561008157018035906001600160401b0382116100815760200191602082023603831361008157565b6001600160401b03811161026d5760208091020190565b805b0361008157565b905035906101c482610343565b9092919261036e6103698261032c565b610272565b938185526020808601920283019281841161008157915b8383106103925750505050565b602080916103a0848661034c565b815201920191610385565b9080601f830112156100815781602061017993359101610359565b6001600160401b038116610345565b905035906101c4826103c6565b909291926103f26103698261032c565b938185526020808601920283019281841161008157915b8383106104165750505050565b6020809161042484866103d5565b815201920191610409565b9080601f8301121561008157816020610179933591016103e2565b919091604081840312610081576104616040610272565b9281356001600160401b038111610081578161047e9184016103ab565b845260208201356001600160401b0381116100815761049d920161042f565b6020830152565b61017990369061044a565b906104b86102a6565b5060006104e36104de6104d46104cd8461021f565b85876102da565b60208101906102f6565b905090565b6104f36104ef8361021f565b9190565b1461051f57610179926105179261050c6105129361021f565b916102da565b6104a4565b6002906105af565b60405163035a803f60e01b8152600490fd5b0390fd5b505061053f600090565b50600190565b634e487b7160e01b600052602160045260246000fd5b6006111561056557565b610545565b906101c48261055b565b634e487b7160e01b600052601160045260246000fd5b9190820391821161059757565b610574565b6105a96101796101799290565b60070b90565b906105b86102a6565b506001906105c58261056a565b6105ce8261056a565b036105d857505090565b6105e2600261056a565b6105eb8261056a565b0361060657505061017990610600600061059c565b90610792565b610610600361056a565b6106198261056a565b0361062957505061017990610c31565b6004906106358261056a565b61063e8261056a565b0361064f5750505061017990610ba6565b61066261065c600561056a565b9161056a565b0361068e5750906106886101799261068261067c84610ccc565b9161021f565b9061058a565b90610c77565b6105319061069b60405190565b6351a1511f60e11b8152918291820190565b601d111561056557565b906101c4826106ad565b610179906106b7565b906106d76103698361032c565b918252565b369037565b906101c46106f76106f1846106ca565b9361032c565b601f1901602084016106dc565b9061070d825190565b8110156102f1576020809102010190565b60005b82811061072d57505050565b606082820152602001610721565b906101c461074b6106f1846106ca565b601f19016020840161071e565b60005b82811061076757505050565b60608282015260200161075b565b906101c46107856106f1846106ca565b601f190160208401610758565b6101799161079e6102a6565b506107a9600f6106c1565b906107b4600161021f565b9161084461083e6107c4856106e1565b936107e56000916107dd6107d78461021f565b88610704565b9060070b9052565b806108236107f28861073b565b9760208a015161080a6108048561021f565b8b610704565b5261081d6108178461021f565b8a610704565b50610775565b9701516108386108328361021f565b89610704565b5261021f565b85610704565b50610ae5565b906108596100c86100be845190565b9060005b81811061086a5750505090565b9091926108836100f6600192865160070b815260200190565b92910161085d565b9061017991610105565b906108ab6108a1835190565b8083529160200190565b90816108bd6020830284019460200190565b926000915b8383106108d157505050505090565b909192939460206108f46108ed8385600195038752895161088b565b9760200190565b93019301919392906108c2565b90610179916100af565b906109176108a1835190565b90816109296020830284019460200190565b926000915b83831061093d57505050505090565b909192939460206109596108ed83856001950387528951610901565b930193019193929061092e565b9261099a6109a892610179969461098d608088019260008901906001600160401b03169052565b868203602088015261084a565b908482036040860152610895565b91606081840391015261090b565b905051906101c482610343565b909291926109d36103698261032c565b938185526020808601920283019281841161008157915b8383106109f75750505050565b60208091610a0584866109b6565b8152019201916109ea565b9080601f83011215610081578151610179926020016109c3565b905051906101c4826103c6565b90929192610a476103698261032c565b938185526020808601920283019281841161008157915b838310610a6b5750505050565b60208091610a798486610a2a565b815201920191610a5e565b9080601f8301121561008157815161017992602001610a37565b9190916040818403126100815780516001600160401b0381116100815783610ac7918301610a10565b9260208201516001600160401b038111610081576101799201610a84565b91610b1e610b2392610b3894610b1261017997610b006102a6565b50604051958694602086019485610966565b9081038252038261024c565b610b86565b6020610b2d825190565b818301019101610a9e565b90610ce1565b6001600160401b03811161026d57602090601f01601f19160190565b906106d761036983610b3e565b3d15610b8157610b763d610b5a565b903d6000602084013e565b606090565b60008091610b92606090565b5080519060200160575afa50610179610b67565b61017990610bb26102a6565b50610bbd60106106c1565b610bc7600161021f565b90610c2b610c26610bd78461073b565b936020860151610bfe6000928392610bf16108178561021f565b5261081d6108328461021f565b960151610c0d6107d78361021f565b52610c20610c1a8261021f565b87610704565b5061021f565b6106e1565b90610ae5565b61017990610c3d6102a6565b50610bbd60116106c1565b610c556101796101799290565b6001600160401b031690565b6105a9610179610179926001600160401b031690565b61017991610c836102a6565b50610c8e60126106c1565b90610c99600161021f565b9161084461083e610cba610cb5610caf876106e1565b95610c48565b610c61565b6107e56000916107dd6107d78461021f565b602061017991610cda600090565b5001515190565b9061017990610cee6102a6565b5061049d610cfa610286565b93845256fea26469706673582212205d5073745206df26a75df5c0f5df9ec450dbca9b78fe5cf7b5e11c334bc56e3464736f6c63430008130033',
                     'contractName': 'ReLULayer',
                     'deployedBytecode': '0x6080604052600436101561001257600080fd5b60003560e01c80632aa40d861461004d578063645fae9814610048578063b99ce9fc146100485763f945adab03610081576101f1565b6101c6565b61018d565b909182601f83011215610081578135916001600160401b03831161008157602001926020830284011161008157565b600080fd5b906020828203126100815781356001600160401b038111610081576100ab9201610052565b9091565b906100cf6100c86100be845190565b8084529260200190565b9260200190565b9060005b8181106100e05750505090565b9091926100fd6100f66001928651815260200190565b9460200190565b9291016100d3565b906101146100c86100be845190565b9060005b8181106101255750505090565b9091926101446100f660019286516001600160401b0316815260200190565b929101610118565b80516040808452610179939160209161016891908401906100af565b920151906020818403910152610105565b90565b60208082526101799291019061014c565b34610081576101b56101a96101a3366004610086565b906104af565b6040519182918261017c565b0390f35b600091031261008157565b565b34610081576101d63660046101b9565b6101b56101e161022c565b6040519182918290815260200190565b34610081576101b561020d610207366004610086565b90610535565b60405191829182901515815260200190565b6101796101796101799290565b610179600061021f565b634e487b7160e01b600052604160045260246000fd5b90601f01601f191681019081106001600160401b0382111761026d57604052565b610236565b906101c461027f60405190565b928361024c565b6101796040610272565b610298610286565b906060825260606020830152565b610179610290565b634e487b7160e01b600052603260045260246000fd5b903590603e193682900301821215610081570190565b908210156102f157602061017992028101906102c4565b6102ae565b903590601e19368290030182121561008157018035906001600160401b0382116100815760200191602082023603831361008157565b6001600160401b03811161026d5760208091020190565b805b0361008157565b905035906101c482610343565b9092919261036e6103698261032c565b610272565b938185526020808601920283019281841161008157915b8383106103925750505050565b602080916103a0848661034c565b815201920191610385565b9080601f830112156100815781602061017993359101610359565b6001600160401b038116610345565b905035906101c4826103c6565b909291926103f26103698261032c565b938185526020808601920283019281841161008157915b8383106104165750505050565b6020809161042484866103d5565b815201920191610409565b9080601f8301121561008157816020610179933591016103e2565b919091604081840312610081576104616040610272565b9281356001600160401b038111610081578161047e9184016103ab565b845260208201356001600160401b0381116100815761049d920161042f565b6020830152565b61017990369061044a565b906104b86102a6565b5060006104e36104de6104d46104cd8461021f565b85876102da565b60208101906102f6565b905090565b6104f36104ef8361021f565b9190565b1461051f57610179926105179261050c6105129361021f565b916102da565b6104a4565b6002906105af565b60405163035a803f60e01b8152600490fd5b0390fd5b505061053f600090565b50600190565b634e487b7160e01b600052602160045260246000fd5b6006111561056557565b610545565b906101c48261055b565b634e487b7160e01b600052601160045260246000fd5b9190820391821161059757565b610574565b6105a96101796101799290565b60070b90565b906105b86102a6565b506001906105c58261056a565b6105ce8261056a565b036105d857505090565b6105e2600261056a565b6105eb8261056a565b0361060657505061017990610600600061059c565b90610792565b610610600361056a565b6106198261056a565b0361062957505061017990610c31565b6004906106358261056a565b61063e8261056a565b0361064f5750505061017990610ba6565b61066261065c600561056a565b9161056a565b0361068e5750906106886101799261068261067c84610ccc565b9161021f565b9061058a565b90610c77565b6105319061069b60405190565b6351a1511f60e11b8152918291820190565b601d111561056557565b906101c4826106ad565b610179906106b7565b906106d76103698361032c565b918252565b369037565b906101c46106f76106f1846106ca565b9361032c565b601f1901602084016106dc565b9061070d825190565b8110156102f1576020809102010190565b60005b82811061072d57505050565b606082820152602001610721565b906101c461074b6106f1846106ca565b601f19016020840161071e565b60005b82811061076757505050565b60608282015260200161075b565b906101c46107856106f1846106ca565b601f190160208401610758565b6101799161079e6102a6565b506107a9600f6106c1565b906107b4600161021f565b9161084461083e6107c4856106e1565b936107e56000916107dd6107d78461021f565b88610704565b9060070b9052565b806108236107f28861073b565b9760208a015161080a6108048561021f565b8b610704565b5261081d6108178461021f565b8a610704565b50610775565b9701516108386108328361021f565b89610704565b5261021f565b85610704565b50610ae5565b906108596100c86100be845190565b9060005b81811061086a5750505090565b9091926108836100f6600192865160070b815260200190565b92910161085d565b9061017991610105565b906108ab6108a1835190565b8083529160200190565b90816108bd6020830284019460200190565b926000915b8383106108d157505050505090565b909192939460206108f46108ed8385600195038752895161088b565b9760200190565b93019301919392906108c2565b90610179916100af565b906109176108a1835190565b90816109296020830284019460200190565b926000915b83831061093d57505050505090565b909192939460206109596108ed83856001950387528951610901565b930193019193929061092e565b9261099a6109a892610179969461098d608088019260008901906001600160401b03169052565b868203602088015261084a565b908482036040860152610895565b91606081840391015261090b565b905051906101c482610343565b909291926109d36103698261032c565b938185526020808601920283019281841161008157915b8383106109f75750505050565b60208091610a0584866109b6565b8152019201916109ea565b9080601f83011215610081578151610179926020016109c3565b905051906101c4826103c6565b90929192610a476103698261032c565b938185526020808601920283019281841161008157915b838310610a6b5750505050565b60208091610a798486610a2a565b815201920191610a5e565b9080601f8301121561008157815161017992602001610a37565b9190916040818403126100815780516001600160401b0381116100815783610ac7918301610a10565b9260208201516001600160401b038111610081576101799201610a84565b91610b1e610b2392610b3894610b1261017997610b006102a6565b50604051958694602086019485610966565b9081038252038261024c565b610b86565b6020610b2d825190565b818301019101610a9e565b90610ce1565b6001600160401b03811161026d57602090601f01601f19160190565b906106d761036983610b3e565b3d15610b8157610b763d610b5a565b903d6000602084013e565b606090565b60008091610b92606090565b5080519060200160575afa50610179610b67565b61017990610bb26102a6565b50610bbd60106106c1565b610bc7600161021f565b90610c2b610c26610bd78461073b565b936020860151610bfe6000928392610bf16108178561021f565b5261081d6108328461021f565b960151610c0d6107d78361021f565b52610c20610c1a8261021f565b87610704565b5061021f565b6106e1565b90610ae5565b61017990610c3d6102a6565b50610bbd60116106c1565b610c556101796101799290565b6001600160401b031690565b6105a9610179610179926001600160401b031690565b61017991610c836102a6565b50610c8e60126106c1565b90610c99600161021f565b9161084461083e610cba610cb5610caf876106e1565b95610c48565b610c61565b6107e56000916107dd6107d78461021f565b602061017991610cda600090565b5001515190565b9061017990610cee6102a6565b5061049d610cfa610286565b93845256fea26469706673582212205d5073745206df26a75df5c0f5df9ec450dbca9b78fe5cf7b5e11c334bc56e3464736f6c63430008130033',
                     'deployedLinkReferences': {},
                     'linkReferences': {},
                     'sourceName': 'contracts/lib/layers-new/ReLULayer.sol'}
