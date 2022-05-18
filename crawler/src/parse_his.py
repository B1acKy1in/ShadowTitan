import json
import requests

class FundHis:
    def __init__(self, code, ljjz, dwjz):
        self.code = code
        self.dwjz = dwjz
        self.ljjz = ljjz

def parse_ljjz(data:str):
    d = data.strip("[").strip("]").split(",")
    # print(d[1])
    if d[1] == 'null':
        d[1] = 0.0
    else:
        d[1] = float(d[1])
    return d

def parse_dwjz(dwjz:dict):
    dwjz['x'] = str(dwjz['x'])
    for key in dwjz:
        if dwjz[key] == '':
            if key != 'y' or key != 'equityReturn':
                dwjz[key] = 'None'
            else:
                dwjz[key] =0.0

    return dwjz

def parse_his(code:str):
    r = requests.get("http://fund.eastmoney.com/pingzhongdata/{}.js".format(code))
    data = r.text
    data = data.replace("/*", "\r\n/*")
    strs = data.split("\r\n")

    dwjz_str = ""
    ljjz_str = ""

    for i in strs:
        if 'Data_netWorthTrend' in i:
            dwjz_str = i
        elif 'Data_ACWorthTrend' in i:
            ljjz_str = i
        else:
            continue

    dwjz_str_list = dwjz_str[dwjz_str.index("= [")+3:]\
        .strip("];")\
        .replace("},{", "}@@{")\
        .split("@@")

    ljjz_str_list = ljjz_str[ljjz_str.index("= [")+3:]\
        .strip("];")\
        .replace("],[", "]@@[")\
        .split("@@")

    ljjz = list(map(parse_ljjz, ljjz_str_list))
    dwjz = list(map(lambda x: json.loads(x), dwjz_str_list))
    dwjz = list(map(parse_dwjz, dwjz))

    fund = FundHis(code, ljjz, dwjz)

    return fund
