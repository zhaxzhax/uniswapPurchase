from web3 import Web3

SETTING = {
    #infra节点地址，需要向infra申请(需要更改)
    "MAINNET_URL": "https://mainnet.infura.io/v3/XXXXXXXXXXXXXXXX",

    #抢币脚本合约的合约地址(不能更改) 
    "CONTRACT_ADDRESS": "0x6e38cD99D54673C04f9599D734c37C1afFd8CA94",

    #钱包私钥，注:钱包私钥切勿外传。本程序只会用私钥签署交易，不会获取您的私钥。(需要更改)
    "WALLET_PRIVATEKEY": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",

    #钱包地址(需要更改)
    "WALLET_ADDRESS": "0xfD51efXXXXXXd8CC703DEXXXXXXXX072C44EE554",

    #一次循环的间隔时间 (可以更改，但不建议更改)
    "TIME_SPAN": 13,

    #希望交换的目标代币的合约地址 注意一定要是有大小写的合约地址，全是小写的是不行的。(需要更改，也就是说在这里填入你想抢购的代币的地址)
    "AIMTOKEN_ADDRESS":"0xfD51efXXXXXXd8CC703DEXXXXXXXX072C44EE554",

    #希望交换的以太币数量(自定义自己购买的数量，这里的示例是购买1.01个以太币)
    "ETHER_AMOUNT":1.01,

    #额外提供gas费可以保证交易被更快打包，默认值为2 (自定义自己愿意付的额外gas费，这里的示例是gas价格比起现在的网络价格高出2Gwei)
    "moreGas":"2"

    ###祝大家能抢上刚上uniswap的代币，如果通过了这个脚本获取了收益的话也可以给我捐赠以太币。捐赠地址为合约地址，也就是0x6e38cD99D54673C04f9599D734c37C1afFd8CA94。
}

w3 = Web3(Web3.HTTPProvider(SETTING["MAINNET_URL"]))


def sendTransation(tx_dic):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)


def sendTransationWithMoreGas(tx_dic, gwei):
    nonce = w3.eth.getTransactionCount(SETTING["WALLET_ADDRESS"])
    tx_dic["nonce"] = nonce
    tx_dic['gasPrice'] = w3.eth.gasPrice + w3.toWei(gwei, 'gwei')
    sign_tx = w3.eth.account.signTransaction(tx_dic, private_key=SETTING["WALLET_PRIVATEKEY"])
    return w3.eth.sendRawTransaction(sign_tx.rawTransaction)