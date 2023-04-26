from elliptic_sdk import AML
from elliptic_sdk.settings import settings
from elliptic_sdk.schemas import LegacyWalletPayload
from elliptic_sdk.schemas import LegacyWalletSubject


def test_aml_wallet_legacy():
    aml = AML(
        api_key=settings.api_key,
        api_secret=settings.api_secret
    )
    result = aml.legacy_wallet(LegacyWalletPayload(
        subject=LegacyWalletSubject(
            asset='ETH',
            blockchain='ethereum',
            hash='0x5024F9a1dED8f675138F473d69BC8848eAA37901'
        ),
        customer_reference='1'
    ))
    assert(result.risk_score == 9.999999999999996)


def test_aml_wallet_legacy_none():
    aml = AML(
        api_key=settings.api_key,
        api_secret=settings.api_secret
    )
    result = aml.legacy_wallet(LegacyWalletPayload(
        subject=LegacyWalletSubject(
            asset='ETH',
            blockchain='ethereum',
            hash='0x30741289523c2e4d2a62c7d6722686d14e723851'
        ),
        customer_reference='1'
    ))
    assert(result.risk_score is None)
