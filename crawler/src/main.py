import time
import datetime
import requests
from json import loads
from fastapi import FastAPI

from parse_his import parse_his
from save import save_fund_info, save_fund_daily, save_fund_his, get_fund_list


app = FastAPI()
app.cache = {'date':float(),'funds':[]}

@app.get('/api/update_fund_his')
async def update_fund_his(code: str = ""):
    # do parameter check before use update
    data = parse_his(code)
    save_fund_his(data)


@app.get('/api/update_fund_info')
async def update_fund_info():
    check_daily_cache()

    save_fund_info(app.cache['funds'])


@app.get('/api/update_fund_daily')
async def update_fund_daily():
    check_daily_cache()
    save_fund_daily(app.cache['funds'])


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

async def check_daily_cache():
    today = time.mktime(datetime.date.today().timetuple())
    if app.cache['date'] is not None and app.cache['date'] < today:
        app.cache['funds'].clear()
        app.cache['date'] = today

    if len(app.cache['funds']) == 0:
        r = requests.get("http://172.18.0.2:9999/api/update_fund_base_info")
        r.encoding = "utf-8"
        l = loads(r.text).strip("[").strip("]")
        l = l.replace("}, {", "}@{").split("@")

        fs = list(map(loads, l))
        fs = list(map(parse_fund_daily, fs))
        app.cache['funds'] = fs
