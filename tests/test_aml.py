"""Elliptic SDK tests/test_aml.py."""
from typing import Union

import pytest

from elliptic_sdk import AML
from elliptic_sdk.schemas import LegacyWalletPayload, LegacyWalletSubject
from elliptic_sdk.settings import settings


@pytest.mark.parametrize(
    'subject_hash,risk_score',
    [
        ('0x5024F9a1dED8f675138F473d69BC8848eAA37901', 9.999999999999996),
        ('0x30741289523c2e4d2a62c7d6722686d14e723851', None),
    ],
)
def test_aml_wallet_single_analysis_risk_score(
    subject_hash: str,
    risk_score: Union[float, None],
):
    """Test AML legacy wallet.

    Args:
        subject_hash: Ethereum wallet address
        risk_score: Expected risk score
    """
    aml = AML(
        api_key=settings.api_key,
        api_secret=settings.api_secret,
    )
    legacy_wallet = aml.wallet_single_analysis(
        LegacyWalletPayload(
            subject=LegacyWalletSubject(
                asset='ETH',
                blockchain='ethereum',
                hash=subject_hash,
            ),
            customer_reference='1',
        ),
    )
    assert legacy_wallet.risk_score == risk_score
