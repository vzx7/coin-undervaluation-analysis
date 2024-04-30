import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

APP_TITLE = 'Undervalued coins'

# token data-api.cryptocompare.com
API_TOKEN = os.getenv("API_TOKEN")

# token github
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# BTC emission
BTC_EMISSION = 21000000

# BTC symbol
BTC_ID = 'BTC'

# Cryptocurrency dictionary, { symbol: emission }
CurrencyList = {
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
    'MATIC': 10000000000,
    'CRV': 3303030299,
    'XMR': 18429993,
    'CRO': 30263013692,
    'TIA': 1039890411,
    'STX': 1818000000,
    'SUI': 10000000000,
    'ETH': 122056395
}

# git repo data
GitHubData = {
    'BTC': {
        'owner': 'bitcoin',
        'repo': 'bitcoin'
    },
    'ETH': {
        'owner': 'ethereum',
        'repo': 'go-ethereum'
    },
    'CRO': {
        'owner': 'crypto-org-chain',
        'repo': 'cronos'
    },
    'SUI': {
        'owner': 'MystenLabs',
        'repo': 'sui'
    },
    'STX': {
        'owner': 'stacks-network',
        'repo': 'stacks-core'
    },
    'TIA': {
        'owner': 'celestiaorg',
        'repo': 'celestia-core'
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