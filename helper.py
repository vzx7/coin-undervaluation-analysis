
import requests
import constants
import calendar
import datetime
 
# Get coin price
def getData(curr):
    url = f"https://data-api.cryptocompare.com/asset/v1/data/by/symbol?asset_symbol={curr}&api_key={constants.API_TOKEN}"
    req = requests.get(url)
    data = req.json()
    return data['Data']

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
        
        date = datetime.datetime.utcnow()
        utc_time = calendar.timegm(date.utctimetuple())

        for v in data:
            # number of committees in the last 90 days
            if v['week'] > utc_time - 7689600 : 
                count_commits += v['total']
    
    return count_commits