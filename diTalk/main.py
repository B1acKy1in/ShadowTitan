from fastapi import FastAPI
from sender import Sender
from typing import Optional
from pydantic import BaseModel

api = "https://oapi.dingtalk.com/robot/send?access_token=e2177eb798b04259a60f2a8484e23f3de388a31be88f8c661cf1ced6b93345ee"

sd = Sender()

app = FastAPI()

@app.get('/test')
async def test():
    sd.sendTextMsg(api,"连通性测试")
    return "success"

class FundMsg(BaseModel):
    msg:str

@app.post('/fund_msg/')
async def fund_msg(msg:FundMsg):
    sd.sendTextMsg(api,msg.msg)
