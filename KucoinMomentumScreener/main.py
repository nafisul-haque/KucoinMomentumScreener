from kucoin.client import Market
import pandas as pd
import numpy as np
import json

client = Market(url = 'https://api.kucoin.com')

klines = pd.DataFrame(client.get_kline('MLS-USDT', '1min'))
tickers = client.get_all_tickers()

period = 12
days = 365
t10_closes = pd.DataFrame(klines.head(period)[2])
print(t10_closes)
t10_closes_list = klines.head(period)[2].tolist()

usdt_pairs = []
i = 0
for i in range(len(usdt_pairs['ticker'])):
    if usdt_pairs['ticker'][i]['symbol'][-4:] == 'USDT':
        tickers.append(usdt_pairs['ticker'][i]['symbol'])
        i += 1
    else:
        continue

def fetch_data():
    all_t10_closes = []
    for i in range(len(usdt_pairs)):
        2



def historical_vol():
    log_returns = []
    j = 1
    for i in range(len(t10_closes_list)):
        if j < 11:
            log_return = np.log(float(t10_closes_list[-j - 1])) / np.log(float(t10_closes_list[-j]))
            log_returns.append(log_return)
            j += 1
        else:
            break

    print(np.std(log_returns))

    av = np.sqrt(days) * np.std(log_returns)
    print(f'{av * 100}%')


