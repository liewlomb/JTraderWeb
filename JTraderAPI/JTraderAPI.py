from fastapi import FastAPI
from requests import request
from function.stock_price_yahoo import *
from function.daily_change import *

app = FastAPI()

@app.get("/stockprice")
async def stockprice(quote:str,startDate:str,endDate:str):
    res = inquiry_stock_price(quote,startDate,endDate)
    return res

@app.get("/dailychange")
async def dailychange(date:str):
    res = daily_change(date)
    return res