from contract import uniswapPurchase
from config import *
import time

if __name__ == '__main__':
        while 1:
            now = int(time.time())
            timeArray = time.localtime(now)
            # 建造交易
            tx_dic_uni = uniswapPurchase(SETTING["AIMTOKEN_ADDRESS"])
            try:
                #估算交易gas消耗，能否成功执行
                tx_dic_gas = w3.eth.estimateGas(tx_dic_uni)
            except Exception as e:
                #打印错误
                 print('writer Reason:', e,time.strftime("%Y--%m--%d %H:%M:%S", timeArray))
            else:
                sendTransationWithMoreGas(tx_dic_uni, SETTING["moreGas"])
                print("已签署交易，请去etherscan上查询自己的交易信息与打包情况，循环跳出")
                break
            ###以太坊的区块13秒一个，建议设置为13秒一个循环
            time.sleep(SETTING["TIME_SPAN"])
