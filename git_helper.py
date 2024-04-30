
import os
import requests

from dotenv import load_dotenv, dotenv_values 

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

Data = {
    'BTC': {
        'owner': 'bitcoin',
        'repo': 'bitcoin'
    },
    'TON': {
        'owner': 'ton-blockchain',
        'repo': 'ton'
    },
    'MIOTA': {
        'owner': 'iotaledger',
        'repo': 'iota-core'
    },
    'SOL': {
        'owner': 'solana-labs',
        'repo': 'solana'
    },
    'XRP': {
        'owner': 'XRPLF',
        'repo': 'rippled'
    },
    'AVAX': {
        'owner': 'ava-labs',
        'repo': 'avalanchego'
    },
    'TRX': {
        'owner': 'tronprotocol',
        'repo': 'java-tron'
    },
    'DOT': {
        'owner': 'paritytech',
        'repo': 'polkadot-sdk'
    },
    'LINK': {
        'owner': 'smartcontractkit',
        'repo': 'chainlink'
    },
    'HBAR': {
        'owner': 'hashgraph',
        'repo': 'hedera-services'
    },
    'APT': {
        'owner': 'aptos-labs',
        'repo': 'aptos-core'
    },
    'FIL': {
        'owner': 'filecoin-project',
        'repo': 'lotus'
    },
    'XLM': {
        'owner': 'stellar',
        'repo': 'stellar-core'
    },
    'ATOM': {
        'owner': 'cosmos',
        'repo': 'cosmos'
    },
    'VET': {
        'owner': 'vechain',
        'repo': 'thor'
    },
    'OP': {
        'owner': 'ethereum-optimism',
        'repo': 'optimism'
    },
    'GRT': {
        'owner': 'graphprotocol',
        'repo': 'graph-node'
    },
    'FTM': {
        'owner': 'Fantom-foundation',
        'repo': 'go-opera'
    },
    'ALGO': {
        'owner': 'algorand',
        'repo': 'go-algorand'
    },
    'FLOW': {
        'owner': 'onflow',
        'repo': 'flow-go'
    },
    'HNT': {
        'owner': 'helium',
        'repo': 'oracles'
    },
    'IOTX': {
        'owner': 'iotexproject',
        'repo': 'iotex-core'
    },
    'HOT': {
        'owner': 'holochain',
        'repo': 'holochain-rust'
    },
    'ZEC': {
        'owner': 'zcash',
        'repo': 'zcash'
    },
    'NANO': {
        'owner': 'nanocurrency',
        'repo': 'nano-node'
    },
    'ONT': {
        'owner': 'ontio',
        'repo': 'ontology'
    },
    'NEAR': {
        'owner': 'near',
        'repo': 'nearcore'
    },
    'MATIC': {
        'owner': 'maticnetwork',
        'repo': 'bor'
    },
    'CRV': {
        'owner': 'curvefi',
        'repo': 'curve-js'
    },
    'XMR': {
        'owner': 'monero-project',
        'repo': 'monero'
    }
}
# Get commits count form base repo
def getCountCommits(curr):
    count_commits = 0
    curr_repo = Data.get(curr)
    if curr_repo != None:
        url = f"https://api.github.com/repos/{curr_repo['owner']}/{curr_repo['repo']}/stats/commit_activity"

        params = {
            "state": "open",
        }

        headers = {'Authorization': f'token {GITHUB_TOKEN}'}
        req = requests.get(url, headers=headers, params=params)
        data = req.json()
        for v in data:
            count_commits += v['total']
    
    return count_commits