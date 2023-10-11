import json
from typing import (
    Optional
)

from web3 import Web3, Account
from web3.types import (
    TxReceipt
)

from .types import (
    AddressLike, 
    Address
)
from .constants import (
    ZERO_ADDRESS
)
from .utils import (
    _load_contract,
    _sign_and_send_transaction
)
from .decorators import (
    needs_private_key
)

class Pinksale:
    def __init__(
        self,
        contract: AddressLike,
        private_key:  Optional[str] = None,
        provider: Optional[str] = None,
        web3: Optional[Web3] = None,
    ) -> None:
        """
        :param contract: Presale contract address. Each presale event has a different contract address.
        :private_key: The private key of the ETH wallet to use.
        :param provider: You can optionally set to a RPC URI.
        :param web3: You can optionally set to a custom Web3 object.
        """

        if web3:
            self.w3 = web3
        else:
            self.w3 = Web3(Web3.HTTPProvider(provider, request_kwargs={"timeout": 60}))

        self.pinksale_ca = _load_contract(self.w3, "pinksale", contract)
        if private_key:
            self.private_key = private_key
            self.address     = Account.from_key(self.private_key).address
        else:
            self.private_key = None
    
    def get_pool_details(
        self
    ) -> dict:
        data = self.pinksale_ca.functions.poolStates().call()
        return {
            "total_raised": data[3],
            "details": json.loads(data[7]),
            "kyc": json.loads(data[-1])
        }
    

    def get_pool_settings(
        self
    ) -> dict:
        data = self.pinksale_ca.functions.poolSettings().call()
        keys = ["token", "currency", "start_time", "end_time", "soft_cap", "total_selling_tokens", "max_contribution", "unknown"]
        return dict(zip(keys, data)) # I don't understand what the last parameter means


    @needs_private_key
    def contribute(
        self,
        amount: int or float
    ) -> TxReceipt: 
        transaction = self.pinksale_ca.functions.contribute(0, ZERO_ADDRESS)
        tx_receipt = _sign_and_send_transaction(
            self.w3, 
            amount,
            transaction, 
            self.address, 
            self.private_key
        )
        return tx_receipt


    def get_pool_owner(
        self
    ) -> Address:
        return self.pinksale_ca.functions.owner().call()
    

    def get_current_rate(
        self
    ) -> int:
        return self.pinksale_ca.functions.currentRate().call()
    

    def get_contribution_of(
        self,
        address: AddressLike
    ) -> int :
        address = Web3.to_checksum_address(address)
        return self.pinksale_ca.functions.contributionOf(address).call()


    @needs_private_key
    def claim(
        self 
    ) -> TxReceipt:
        transaction = self.pinksale_ca.functions.claim()
        tx_receipt  = _sign_and_send_transaction(self.w3, 0, transaction, self.address, self.private_key)
        return tx_receipt


    @needs_private_key
    def emergency_withdraw(
        self,
    ) -> TxReceipt:
        transaction = self.pinksale_ca.functions.emergencyWithdrawContribution()
        tx_receipt  = _sign_and_send_transaction(self.w3, 0, transaction, self.address, self.private_key)
        return tx_receipt


    def get_contributor_count(
        self
    ) -> int:
        return self.pinksale_ca.functions.getContributorCount().call()
    

    def get_contributors(
        self,
        start_index: int,
        end_index: int
    ) -> list:
        return self.pinksale_ca.functions.getContributors(start_index, end_index).call()

    
    def get_all_contributors(
        self
    ) -> list:
        start, end = 0, self.get_contributor_count()
        return self.pinksale_ca.functions.getContributors(start, end).call()
