# elliptic-sdk

Elliptic API

_initial implementation for Elliptic AML API_

## roadmap

- support async methods
- support all AML methods
- tests coverage

## install

```shell
pip install elliptic_sdk
```

| Variable            | Default | Comments |
|---------------------|---------|----------|
| ELLIPTIC_API_KEY    |         |          |
| ELLIPTIC_API_SECRET |         |          |

## Usage

```python
from elliptic_sdk import AML
from elliptic_sdk.schemas import LegacyWalletPayload
from elliptic_sdk.schemas import LegacyWalletSubject

aml = AML(
    api_key='api-key-here',
    api_secret='api-secret-here'
)

result = aml.wallet_single_analysis(
    LegacyWalletPayload(
        subject=LegacyWalletSubject(
            asset='ETH',
            blockchain='ethereum',
            hash='0x5024F9a1dED8f675138F473d69BC8848eAA37901'
        ),
        customer_reference='1'
    )
)
print(result.risk_score)
```
