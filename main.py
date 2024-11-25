import random
import time
import tqdm
import tabulate
import helper
import constants
import datetime
from babel.numbers import format_currency, format_decimal


print('\n### ' + constants.APP_TITLE.title() + ' ###\n')

date = datetime.datetime.today()
print('Date: ',  date.strftime("%m/%d/%Y, %H:%M:%S"))

#BTC_price = 63000
BTC_DATA = helper.getData(constants.BTC_ID)
BTC_price = BTC_DATA['PRICE_USD']
BTC_TOTAL_MKT_CUP = BTC_DATA['TOTAL_MKT_CAP_USD']
"""
Dictionary Underestimate
"""
Underestimate = {}

for curr, emission in tqdm.tqdm(constants.CurrencyList.items()): 
    time.sleep(1)
    curr_data = helper.getData(curr)

    if len(curr_data) == 0:
        continue
    
    total_mkt_cap = curr_data['TOTAL_MKT_CAP_USD']
    currency_price = curr_data['PRICE_USD']
    #currency_price = random.randint(1, 100)
    underestimate = (BTC_price/(emission/constants.BTC_EMISSION))/currency_price
    #print(curr, currency_price, underestimate)
    count_commits = helper.getCountCommits(curr)
    Underestimate[underestimate] = [curr, currency_price, count_commits, emission, total_mkt_cap]
    
sorted_underestimate = dict(sorted(Underestimate.items(), reverse=True))

BTC_commits = helper.getCountCommits(constants.BTC_ID)

underestimate_final = [];

for v, data in sorted_underestimate.items():
    commits = data[2] if data[2] > 0 else 'no data'
    underestimate_final.append([data[0], format_decimal(data[3], format='#,##0.##;-#', locale='en'), format_currency(data[4], 'USD', locale='en_US'), '$' + str(round(data[1], 4)), commits, round(v)])

underestimate_final.append([
    constants.BTC_ID, format_decimal(constants.BTC_EMISSION, format='#,##0.##;-#', locale='en'), format_currency(BTC_TOTAL_MKT_CUP, 'USD', locale='en_US'), format_currency(BTC_price, 'USD', locale='en_US'), BTC_commits, 0
])

print('\n' + tabulate.tabulate(underestimate_final, headers=["Ind", "Simbol", "Emission", "Mkt. Cap.", "Price (USD)", "GIT commits of 90 days", "Underestimate"], showindex="always", tablefmt="double_grid"))

