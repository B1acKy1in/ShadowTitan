from fastapi import FastAPI
from fund import get_fund_base_info
from wh import get_wh_daily_price

app = FastAPI()

@app.get('/api/update_fund_base_info')
async def update_fund_base_info():
    return get_fund_base_info()

@app.get('/api/get_wh_price')
async def get_wh_price():
    return get_wh_daily_price()