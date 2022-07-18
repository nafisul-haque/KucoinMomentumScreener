from kucoin.client import Market
import pandas as pd
import numpy as np
import json

client = Market(url = 'https://api.kucoin.com')

klines = pd.DataFrame(client.get_kline('BTC-USDT', '1min'))
tickers = client.get_all_tickers()

#print(klines.head(10))

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

keys = list(tickers.keys())
keys_t = tickers

i = 0
t = []
print(range(len(tickers['ticker'])))
for i in range(len(tickers['ticker'])):
    t.append(tickers['ticker'][i]['symbol'])
    i += 1

#print(tickers['ticker'][0]['symbol'])
print(len(t))