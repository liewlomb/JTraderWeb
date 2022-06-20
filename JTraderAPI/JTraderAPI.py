from fastapi import FastAPI
from requests import request
from function.stock_price_yahoo import *
from function.daily_change import *
from function.above_ema import *
from function.buying_recovery import *
from function.market_anomaly import *

app = FastAPI()

@app.get("/stockprice")
async def stockprice(quote:str,startDate:str,endDate:str):
    res = inquiry_stock_price(quote,startDate,endDate)
    return res

@app.get("/dailychange")
async def dailychange(date:str):
    res = daily_change(date)
    return res

@app.get("/aboveema")
async def aboveema(emaLength:str,beginDate:str,endDate:str):
    res = above_ema(emaLength,beginDate,endDate)
    return res

@app.get("/buyingRecovery")
async def buyingRecovery(endDate:str,setRange:str):
    res = buying_recovery(endDate,setRange)
    return res

@app.get("/marketAnomaly")
async def marketAnomaly(quote:str,beginYear:str,endYear:str,period:str):
    res = market_anomaly(quote,beginYear,endYear,period)
    return res