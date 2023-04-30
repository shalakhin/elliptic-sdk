"""Elliptic SDK elliptic_sdk/enums.py."""
import enum


class WalletAnalysisSubjectTypeEnum(enum.Enum):
    """WalletAnalysisSubjectType enum.

    https://developers.elliptic.co/reference/post_wallet-synchronous
    """

    ADDRESS = 'address'


class LegacyWalletPayloadTypeEnum(enum.Enum):
    """LegacyWalletPayload enum.

    https://developers.elliptic.co/reference/post_wallet-synchronous
    """

    WALLET_EXPOSURE = 'wallet_exposure'
