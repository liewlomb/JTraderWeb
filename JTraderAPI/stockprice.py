from fastapi import FastAPI
from function.stock_price_yahoo import *

app = FastAPI()

@app.get("/stockprice")
def stockprice(quote:str,startDate:str,endDate:str):
    res = inquiry_stock_price(quote,startDate,endDate)
    return res