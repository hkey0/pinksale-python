import json
import os

from web3 import Web3
from web3.contract import Contract
from web3.types import (
    TxData,
    TxReceipt
)

from .types import AddressLike


def _get_abi(ca_type: str) -> dict:
    with open(f"{os.path.dirname(os.path.abspath(__file__))}/assets/{ca_type}.json", "r") as f:
        abi: str = json.load(f)
    return abi


def _load_contract(
        w3: Web3, 
        ca_type: str,
        address: AddressLike
    ) -> Contract:
    address = Web3.to_checksum_address(address)
    return w3.eth.contract(address=address, abi=_get_abi(ca_type))


def _sign_and_send_transaction(
        w3: Web3, 
        amount: float or int, 
        tx: TxData, 
        wallet: AddressLike, 
        priv_key: str
    ) -> TxReceipt:
    nonce = w3.eth.get_transaction_count(wallet)
    txn = tx.build_transaction({
        "from": wallet,
        "nonce": nonce,
        'gas': 700000,
        "gasPrice": w3.to_wei('5', 'gwei'),
        "value": w3.to_wei(amount, 'ether'),
    })

    gas_estimate = w3.eth.estimate_gas(txn)
    txn = tx.build_transaction({
        "from": wallet,
        "nonce": nonce,
        'gas': gas_estimate,
        "gasPrice": w3.to_wei('5', 'gwei'),
        "value": w3.to_wei(amount, 'ether'),
    })

    signed_txn = w3.eth.account.sign_transaction(txn, priv_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
    txn_hash = w3.to_hex(txn_hash)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

