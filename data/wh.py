import requests
import time

# headers
SHORT_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36'
}
# url
FX_SPOT_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sp-quot.json"
FX_SWAP_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/rfx-sw-quot.json"
FX_PAIR_URL = "http://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/cpair-quot.json"
# payload
SPOT_PAYLOAD = {
    "t": {}
}

def get_wh_daily_price():
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    # }
    # # url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx"
    payload = {"t": str(int(round(time.time() * 1000)))}
    res = requests.post(FX_SPOT_URL, data=payload, headers=SHORT_HEADERS)
    return res.json()