
# pinksale-python

The unofficial Python client for [Pinksale](https://pinksale.finance).

# Functionalty

- A Python wrapper for any presale contract.
- Easy access to the necessary data about the presale.
- Supports BSC and ETH for now.

#### Supports
- Binance Smart Chain
    - Supports ETH (BNB)

- Ethereum 
    - Supports ETH (ETH)


# Donation
You can support the project by donating :)\
for ETH/BSC/ARBI/AVAX/POLYGON chains: `0x09a27f3647aD2Fd081e515F9D2d785292Fba38C1`
## Usage/Examples

#### Write functions

To make a contribution, you only need to enter the amount in ether:
```python
from pinksale.pinksale import Pinksale


client = Pinksale("0x0A8527e4A1e3f8b56508e26b8Dc332e067916108", "your_private_key", provider="https://bsc-dataseed1.ninicoin.io")
tx_receipt = client.contribute(1) # Contribute with 1 BNB
```

Emergency withdraw:
```py
client.emergency_withdraw()
```

You can claim your tokens when pool finalizes:
```py
client.claim()
```

#### View Functions

A simple call example for view functions. Contract address is your presale address.
```python
from pinksale.pinksale import Pinksale


client = Pinksale("0x0A8527e4A1e3f8b56508e26b8Dc332e067916108", provider="https://bsc-dataseed1.ninicoin.io")
contributors = client.get_all_contributors()
>> ['0x0080b399E21475a7ca6d6cf9081C983BE51Bdead', '0xA8617881a6914b59000f279e4425F0E8E84BeBa5', ...]
```

You can get Pool Details: Total raised, Details (image, links, etc.), KYC
```python
client.get_pool_details()
>> {'total_raised': 120222334187259780175, 'details': {'a': 'https://photos.pinksale.finance/file/pinksale-logo-upload/1696947582061-36b70f470f30f10fb3055f7c2a32ca88.jpg', 'b': 'https://zhaodavinci.com/', 'd': 'https://twitter.com/Zhao_DaVinci', 'e': 'https://github.com/AnalytixAudit/Solidity/blob/main/20231009_AnalytixAudit_ZhaoDaVinc_VINCI_Audit.pdf', 'f': 'https://t.me/ZhaoDaVinci', 'h': "♠️ Hottest Meta of the Month ♠️\nWhy did CZ tokenize the Mona Lisa? To blend Da Vinci's genius with crypto magic, creating a masterpiece of digital value ♠️ Top Trending ♠️ Audited Contract ♠️ Top Tier Listings ♠️ CMC & CG Fast track ♠️ Top Incubator ♠️ Based Team ♠️ Buy Back & Burn ♠️ 100x Target ♠️", 's': 'https://youtu.be/HYnUI5dDyeo'}, 'kyc': {'a': '', 'b': 'https://app.analytixaudit.com/zhao-da-vinc', 'c': '', 'd': '', 'e': '', 'f': ''}}
```

Also pool settings: "token", "currency", "start_time", "end_time", "soft_cap", "total_selling_tokens", "max_contribution"

```py
client.get_pool_settings()
```

Get current rate returns amount of tokens for 1 bnb.
```py
client.get_current_rate()
```

Get all contributor addresses:
```py
client.get_all_contributors()
```

Get contribution amount of an address:
```py
address = ""
client.get_contribution_of(address)
```


# Changelog

_0.1.0_
  - Support for BSC (BNB) and ETH (ETH)
