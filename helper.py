
import requests
import constants
 
# Get coin price
def getPrice(curr):
    url = f"https://data-api.cryptocompare.com/asset/v1/data/by/symbol?asset_symbol={curr}&api_key={constants.API_TOKEN}"
    req = requests.get(url)
    data = req.json()
    return data['Data']['PRICE_USD']

# Get commits count form base repo
def getCountCommits(curr):
    count_commits = 0
    curr_repo = constants.GitHubData.get(curr)
    if curr_repo != None:
        url = f"https://api.github.com/repos/{curr_repo['owner']}/{curr_repo['repo']}/stats/commit_activity"

        params = {
            "state": "open",
        }

        headers = {'Authorization': f'token {constants.GITHUB_TOKEN}'}
        req = requests.get(url, headers=headers, params=params)
        data = req.json()
        for v in data:
            count_commits += v['total']
    
    return count_commits