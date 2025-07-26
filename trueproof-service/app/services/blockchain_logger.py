import os
import datetime
from web3 import Web3

# Setup Web3 connection
web3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_RPC_URL")))
contract_address = Web3.to_checksum_address(os.getenv("CONTRACT_ADDRESS"))
contract_abi = [
    {
        "inputs": [
            {"internalType": "string", "name": "fileHash", "type": "string"},
            {"internalType": "string", "name": "verdict", "type": "string"},
            {"internalType": "string", "name": "scannedAt", "type": "string"}
        ],
        "name": "registerFile",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "anonymous": False,
        "inputs": [
            {"indexed": False, "internalType": "string", "name": "fileHash", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "verdict", "type": "string"},
            {"indexed": False, "internalType": "string", "name": "scannedAt", "type": "string"}
        ],
        "name": "FileVerified",
        "type": "event"
    }
]

contract = web3.eth.contract(address=contract_address, abi=contract_abi)
private_key = os.getenv("PRIVATE_KEY")
wallet_address = web3.eth.account.from_key(private_key).address

def log_to_blockchain(file_hash: str, verdict: str):
    timestamp = datetime.datetime.utcnow().isoformat()

    tx = contract.functions.registerFile(file_hash, verdict, timestamp).build_transaction({
        "from": wallet_address,
        "nonce": web3.eth.get_transaction_count(wallet_address),
        "gas": 300000,
        "gasPrice": web3.to_wei("10", "gwei")
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.to_hex(tx_hash)