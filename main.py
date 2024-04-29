
import urllib.request, json
import random
import time
import tqdm
import tabulate

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
Получить цену монеты
 """
def getPrice(curr):
    url = f"https://data-api.cryptocompare.com/asset/v1/data/by/symbol?asset_symbol={curr}&api_key="

    with urllib.request.urlopen(url) as url:
        data = json.load(url)
        return data['Data']['PRICE_USD']


BTC_price = getPrice(BTC_ID)

Profit = {}

for curr, emission in tqdm.tqdm(Currency.items()): 
    time.sleep(2)
    currency_price = getPrice(curr)
    #currency_price = random.randint(1, 100)
    
    underestimate = (BTC_price/(emission/BTC_EMISSION))/currency_price
    print(curr, currency_price, underestimate)
    Profit[round(underestimate)] = curr
    
sorted_profit = dict(sorted(Profit.items(), reverse=True))

_underestimate = [];
for v, k in sorted_profit.items():
    _underestimate.append([k,v])

print(tabulate.tabulate(_underestimate, headers=["Ind", "Simbol", "Underestimate"], showindex="always", tablefmt="double_grid"))