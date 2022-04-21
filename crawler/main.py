import requests
from json import loads
from s import save_fund

def parse_fund_daily(fs:dict):
    if fs.get('dwzz') == None :
            fs['dwzz'] = 10.0

    if fs.get('ljzz') == None :
        fs['ljzz'] = 10.0

    fs["ljjz"] = float(fs.get("ljjz"))
    fs["dwjz"] = float(fs.get("dwjz"))
    fs["dwzz"] = float(fs.get("dwzz"))
    fs["ljzz"] = float(fs.get("ljzz"))
    return fs

def update_fund_daily():
    r = requests.get("http://172.18.0.2:9999/api/update_fund_base_info")
    r.encoding = "utf-8"
    l = loads(r.text).strip("[").strip("]")
    l = l.replace("}, {", "}@{").split("@")
    funds = list(map(loads, l))
    funds = list(map(parse_fund_daily, funds))

    # print(funds[1])
    save_fund(funds)

def catch_funds_history():
    # r = requests.get("http://localhost:8080/public/fund_open_fund_info_em/", data=data)
    # r = requests.get("http://localhost:8080/public/fund_open_fund_info_em?fund=161226&indicator=单位净值走势")
    r = requests.get("http://fund.eastmoney.com/pingzhongdata/710001.js")
    print(r.text)


def main():
    # catch_funds_history()
    update_fund_daily()

if __name__ == "__main__":
    main()
