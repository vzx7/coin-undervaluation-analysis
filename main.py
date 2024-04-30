import random
import time
import tqdm
import tabulate
import helper
import constants

print('\n### ' + constants.APP_TITLE.title() + ' ###\n')

#BTC_price = 63000
BTC_price = helper.getPrice(constants.BTC_ID)
"""
Dictionary Underestimate
"""
Underestimate = {}

for curr, emission in tqdm.tqdm(constants.CurrencyList.items()): 
    time.sleep(1)
    currency_price = helper.getPrice(curr)
    #currency_price = random.randint(1, 100)
    
    underestimate = (BTC_price/(emission/constants.BTC_EMISSION))/currency_price
    #print(curr, currency_price, underestimate)
    count_commits = helper.getCountCommits(curr)
    Underestimate[underestimate] = [curr, currency_price, count_commits, emission]
    
sorted_underestimate = dict(sorted(Underestimate.items(), reverse=True))

BTC_commits = helper.getCountCommits(constants.BTC_ID)

underestimate_final = [[
    constants.BTC_ID, constants.BTC_EMISSION, '$' + str(BTC_price), BTC_commits, 0
]];

for v, data in sorted_underestimate.items():
    commits = data[2] if data[2] > 0 else 'no data'
    underestimate_final.append([data[0], data[3], '$' + str(data[1]), commits, round(v)])

print('\n' + tabulate.tabulate(underestimate_final, headers=["Ind", "Simbol", "Emission", "Price (USD)", "GIT commits", "Underestimate"], showindex="always", tablefmt="double_grid"))

