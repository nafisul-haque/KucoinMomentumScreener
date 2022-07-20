from kucoin.client import Market
import pandas as pd
import numpy as np
import time

client = Market(url = 'https://api.kucoin.com')

klines = pd.DataFrame(client.get_kline('BTC-USDT', '1min'))
tickers = client.get_all_tickers()

period = 12
days = 365
t10_closes = pd.DataFrame(klines.head(period)[2])
t10_closes_list = klines.head(period)[2].values.tolist()
#print(t10_closes_list)

def fetch_tickers():
    usdt_pairs = []
    i = 0
    for i in range(len(usdt_pairs['ticker'])):
        if usdt_pairs['ticker'][i]['symbol'][-4:] == 'USDT':
            tickers.append(usdt_pairs['ticker'][i]['symbol'])
            i += 1
        else:
            continue
    return()

def historical_vol(closes_list):
    log_returns = []
    j = 1
    for i in range(len(t10_closes_list)):
        if j < 11:
            log_return = np.log(float(t10_closes_list[-j - 1])) / np.log(float(t10_closes_list[-j]))
            log_returns.append(log_return)
            j += 1
        else:
            break

    lr_std = np.std(log_returns)
    annualised_vol = np.sqrt(days) * lr_std
    return(annualised_vol)

historical_vol(t10_closes_list)




