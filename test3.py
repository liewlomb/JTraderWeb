import yfinance as yf

result = {}
date = ['2022-06-08','2022-06-09','2022-06-10']
emaLength = '5'
for i in range(len(date)):
    x = date[i]
    setclose = yf.download('^SET.BK', start = x, stop = x)
    setclose.reset_index(inplace=True)
    setclose = setclose['Close']

    setclose = setclose.iloc[0]

    genDict = {i:{'date':date[i],'SET Close Price': setclose,'Above EMA('+emaLength+')': 0}}
    result.update(genDict)
print(result)
