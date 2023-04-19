from elliptic import AML
from elliptic.settings import settings
from elliptic.schemas import LegacyWalletPayload
from elliptic.schemas import LegacyWalletSubject


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
