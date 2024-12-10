import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()

APP_TITLE = 'Undervalued coins'

# token data-api.cryptocompare.com
API_TOKEN = os.getenv("API_TOKEN")

# token github
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

# BTC emission
BTC_EMISSION = 19792881

# BTC symbol
BTC_ID = 'BTC'

# Cryptocurrency dictionary, { symbol: emission }
CurrencyList = {
    'MIOTA': 3229505319,
    'SOL': 476106751,
    'TONCOIN': 2550783411,
    'ADA': 35102215549,
    'AVAX': 447755292,
    'TRX': 86262438049,
    'DOT': 1527202210,
    'LINK': 626849970,
    'UNI': 600483073,
    'HBAR': 38228257945,
    'APT': 536084855,
    'FIL': 609812460,
    'XLM': 30161094439,
    'ATOM': 390930671,
    'VET': 80985041177,
    'OP': 125507049,
    'GRT': 9548531509,
    'FTM': 2803634835,
    'ALGO': 8308506364,
    'FLOW': 1503293597,
    'HNT': 170472132,
    'IOTX': 9441369057,
    'ZEC': 16328268,
    'NANO': 133248297,
    'ROSE': 7064132681,
    'CTK': 133687317,
    'NEAR': 1188295576,
    'POL': 8352869756,
    'CRV': 1250228763 ,
    'XMR': 18429993,
    'CRO': 26571560696,
    'TIA': 446686915,
    'STX': 1818000000,
    'SUI': 2927660018,
    'ETH': 122056395,
    'JUP': 1350000000,
    'W': 2766268902,
    'PYTH': 3624988786,
    'INJ': 98848019,
    'NOT': 102719221714,
    'ARB': 4097359817,
    'CFX': 4723703483,
    'WLD': 754009475,
    'SC': 57769785000,
    'TAO': 21000000,
    'RUNE': 340715380,
    'KSM': 15810529,
    'STRK': 2259283720,
    'SEI': 3982916666,
    'ZK': 3675000000,
    'KAS': 28704026601,
    'OM': 943444109,
    'CFG': 507587217,
    'MPL': 4417985,
    'AEVO': 900249491,
    'RSR': 53473336211,
    'ONDO': 1389759838
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
    'TAO': {
        'owner': 'opentensor',
        'repo': 'bittensor'
    },
    'KSM': {
        'owner': 'paritytech',
        'repo': 'polkadot-sdk'
    },
    'SEI': {
        'owner': 'sei-protocol',
        'repo': 'sei-chain'
    },
    'KAS': {
        'owner': 'kaspanet',
        'repo': 'rusty-kaspa'
    },
    'STRK': {
        'owner': 'starkware-libs',
        'repo': 'cairo'
    },
    'SIA': {
        'owner': 'SiaFoundation',
        'repo': 'renterd'
    },
    'WLD': {
        'owner': 'worldcoin',
        'repo': 'developer-portal'
    },
    'INJ': {
        'owner': 'InjectiveLabs',
        'repo': 'injective-ts'
    },
    'PITH': {
        'owner': 'pyth-network',
        'repo': 'pyth-crosschain'
    },
    'ZK': {
        'owner': 'matter-labs',
        'repo': 'zksync-era'
    },
    'ROSE': {
        'owner': 'oasisprotocol',
        'repo': 'oasis-core'
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
    'TONCOIN': {
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
        'repo': 'substrate-connect'
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
    'CFX': {
        'owner': 'Conflux-Chain',
        'repo': 'conflux-rust'
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
    'ZEC': {
        'owner': 'zcash',
        'repo': 'zcash'
    },
    'NANO': {
        'owner': 'nanocurrency',
        'repo': 'nano-node'
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
    },
    'W': {
        'owner': 'wormhole-foundation',
        'repo': 'wormhole'
    },
    'CFG': {
        'owner': 'centrifuge',
        'repo': 'centrifuge-chain'
    },
    'MPL': {
        'owner': 'maple-labs',
        'repo': 'maple-js'
    },
    'RSR': {
        'owner': 'reserve-protocol',
        'repo': 'register'
    },
    'OM': {
        'owner': 'MANTRA-Chain',
        'repo': 'mantrachain'
    },
    'ONDO': {
        'owner': 'ondoprotocol',
        'repo': 'peggedassets-server'
    }
}
