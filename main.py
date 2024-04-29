
import urllib.request, json
import random
import time
import tqdm
import tabulate
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv() 

MY_TOKEN = os.getenv("MY_TOKEN")

# BTC emission
BTC_EMISSION = 21000000

# BTC symbol
BTC_ID = 'BTC'

""" 
Cryptocurrency dictionary, { symbol: emission }
"""
Currency = {
    'MIOTA': 3229505319,
    'SOL': 574915273,
    'XRP': 100000000000,
    'TON': 5105886521,
    'ADA': 45000000000,
    'AVAX': 715748719,
    'TRX': 87554275200,
    'DOT': 1437953431,
    'BCH': 21000000,
    'LINK': 1000000000,
    'UNI': 1000000000,
    'HBAR': 50000000000,
    'APT': 1093375145,
    'FIL': 1960538665,
    'XLM': 50001806812,
    'ATOM': 390930671,
    'VET': 86712634466,
    'MKR': 1005577,
    'OP': 4294967296,
    'GRT': 10797266751,
    'FTM': 3175000000,
    'ALGO': 10000000000,
    'FLOW': 1503293597,
    'HNT': 223000000,
    'OM': 888888888,
    'IOTX': 10000000000,
    'HOT': 177619433541,
    'ZEC': 21000000,
    'NANO': 133248297,
    'ONT': 1000000000,
    'CTK': 133687317,
    'NEAR': 1188295576,
    'QRL': 105000000,
    'MATIC': 10000000000,
    'CRV': 3303030299,
    'XMR': 18429993
};

""" 
Get coin price
 """
def getPrice(curr):
    url = f"https://data-api.cryptocompare.com/asset/v1/data/by/symbol?asset_symbol={curr}&api_key={MY_TOKEN}"

    with urllib.request.urlopen(url) as url:
        data = json.load(url)
        return data['Data']['PRICE_USD']


BTC_price = getPrice(BTC_ID)
"""
Dictionary Underestimate
"""
Underestimate = {}

for curr, emission in tqdm.tqdm(Currency.items()): 
    time.sleep(2)
    currency_price = getPrice(curr)
    #currency_price = random.randint(1, 100)
    
    underestimate = (BTC_price/(emission/BTC_EMISSION))/currency_price
    print(curr, currency_price, underestimate)
    Underestimate[round(underestimate)] = curr
    
sorted_underestimate = dict(sorted(Underestimate.items(), reverse=True))

underestimate_final = [];
for v, k in sorted_underestimate.items():
    underestimate_final.append([k,v])

print(tabulate.tabulate(underestimate_final, headers=["Ind", "Simbol", "Underestimate"], showindex="always", tablefmt="double_grid"))