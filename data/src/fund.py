from json import dumps
from requests import get

def parse_fund_daily(fs:str):
    temp = fs.strip("[").strip("]")
    ts = temp.split(",")
    fund = {}
    fund["code"] = ts[0]
    fund["full_name"] = ts[1]
    fund["sim_name"] = ts[2]

    dwjz = ts[5][1:-1]
    if len(dwjz) > 0:
        fund["dwjz"] = float(dwjz)
    else:
        fund["dwjz"] = float(0.0)

    ljjz = ts[6][1:-1]
    if len(ljjz) > 0:
        fund["ljjz"] = float(ljjz)
    else:
        fund["ljjz"] = float(0.0)

    fund["sgzt"] = ts[9]
    fund["shzt"] = ts[10]

    return fund

def get_fund_base_info():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
    }
    url = "http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx"
    params = {
        "t": "1",
        "lx": "1",
        "letter": "",
        "gsid": "",
        "text": "",
        "sort": "zdf,desc",
        "page": "1,20000",
        "dt": "1580914040623",
        "atfc": "",
        "onlySale": "0",
    }
    res = get(url, params=params, headers=headers)

    # parse data
    front = res.text.index("datas:[")
    back = res.text.index("],count")
    txt = res.text[front+len("datas:["):back]
    txt = txt.replace("],[", "]##[")

    datas = txt.split("##")

    funds = list(map(parse_fund_daily, datas))
    t = dumps(funds)

    return t