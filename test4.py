import yfinance as yf
from datetime import datetime
from datetime import timedelta
import pandas as pd
import talib as ta
import numpy as np

def construct_month(month):
    if month == 1:
        res = 'Jan'
    elif month == 2:
        res = 'Feb'
    elif month == 3:
        res = 'Mar'
    elif month == 4:
        res = 'Apr'
    elif month == 5:
        res = 'May'
    elif month == 6:
        res = 'Jun'
    elif month == 7:
        res = 'Jul'
    elif month == 8:
        res = 'Aug'
    elif month == 9:
        res = 'Sep'
    elif month == 10:
        res = 'Oct'
    elif month == 11:
        res = 'Nov'
    elif month == 12:
        res = 'Dec'
    return res

def cal_start_date(endDate):
    month = endDate[5:7]
    if month in ['03','04','05','06','07','08','09','10']:
        beginMonth = int(endDate[5:7])-1
        lastM = int(endDate[5:7])-2
        endMonth = int(endDate[5:7])
        startDate = str(endDate[:4])+'-0'+str(int(endDate[5:7])-2)+'-01'
    elif month in ['11','12']:
        beginMonth = int(endDate[5:7])-1
        lastM = int(endDate[5:7])-2
        endMonth = int(endDate[5:7])
        startDate = str(endDate[:4])+'-'+str(int(endDate[5:7])-2)+'-01'
    elif month in ['01']:
        beginMonth = 12
        lastM = 11
        endMonth = int(endDate[5:7])
        startDate = str(int(endDate[:4])-1)+'-11-01'
    elif month in ['02']:
        beginMonth = 1
        lastM = 12
        endMonth = int(endDate[5:7])
        startDate = str(int(endDate[:4])-1)+'-12-01'
    res = {'startDate':startDate,'endDate' :endDate,'beginMonth':beginMonth,'endMonth':endMonth,'lastM':lastM}
    return res 

def buying_recovery(endDate,setRange):
    if setRange == 'SET100':
        stock_list = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set100_q1_2022.csv')
    elif setRange == 'SET50':
        stock_list = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set50_q1_2022.csv')
    elif setRange == 'SET51-100':
        stock_list = pd.read_csv('/home/liewlom/Desktop/JTrader/Data-batch/JTraderAPI/set100/set51_100_q1_2022.csv')
    result = {}
    res = cal_start_date(endDate)
    startDate = res['startDate']
    for i in range(len(stock_list)):
        quote = stock_list.iloc[i]['Quote']
        quote = quote.upper()
        quote = quote.strip()
        
        df = yf.download(quote+'.bk', start = startDate, stop = endDate)
        df.reset_index(inplace=True)
        df['Date'] = pd.to_datetime(df['Date'])
        
        #Last 2 Month Close
        last_month_close = df.loc[df['Date'].dt.month == res['lastM']]
        last_month_close.reset_index(inplace=True)
        last_month_close = last_month_close[['Date','Close']]
        print(quote)
        print('last month')
        print(last_month_close)
        
        #Begin Month
        begin_month = df.loc[df['Date'].dt.month == res['beginMonth']]
        begin_month.reset_index(inplace=True)
        begin_month = begin_month[['Date','Close']]
        print('begin month')
        print(begin_month)
        
        #End Month
        end_month = df.loc[df['Date'].dt.month == res['endMonth']]
        end_month.reset_index(inplace=True)
        beginDate = end_month['Date'][0]
        end_month = end_month.set_index('Date')
        end_month = end_month.loc[beginDate:endDate]
        end_month.reset_index(inplace=True)
        end_month = end_month[['Date','Close']]
        print('end month')
        print(end_month)
        
        
        # Calculate Percent Change
        
        percent_begin = ((begin_month['Close'].iloc[-1] - last_month_close['Close'].iloc[-1])/last_month_close['Close'].iloc[-1])*100
        
        if len(end_month) != 1:
            percent_end = ((end_month['Close'].iloc[-1] - begin_month['Close'].iloc[-1])/begin_month['Close'].iloc[-1])*100
        elif len(end_month) == 1:
            percent_end = ((end_month['Close'].iloc[0] - begin_month['Close'].iloc[-1])/begin_month['Close'].iloc[-1])*100
        
        bm = construct_month(res['beginMonth'])
        em = construct_month(res['endMonth'])
            
        tmp = {quote:{'Selected Date': endDate,'Begin Month' : bm,'%Change '+bm: float('{:.2f}'.format(percent_begin)),'End Month' : em,'%Change '+em: float('{:.2f}'.format(percent_end))}}
        result.update(tmp)
    return result
    


#  Unit Test
endDate = '2022-06-01'
setRange = 'SET50'
print(buying_recovery(endDate,setRange))


