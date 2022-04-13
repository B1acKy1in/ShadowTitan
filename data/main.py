from fastapi import FastAPI
from fund import get_fund_daily
from wh import get_wh_daily_price

app = FastAPI()

@app.get('/api/fund_daily')
async def fund_daily():
    return get_fund_daily()

@app.get('/api/get_wh_price')
async def get_wh_price():
    return get_wh_daily_price()