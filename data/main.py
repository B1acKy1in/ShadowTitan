from fastapi import FastAPI
from fund import get_fund_base_info

app = FastAPI()

@app.get('/api/update_fund_base_info')
async def update_fund_base_info():
    return get_fund_base_info()

