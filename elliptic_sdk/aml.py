"""Elliptic SDK elliptic_sdk/aml.py."""
from .auth import Auth
from .client import get_client
from .schemas import LegacyWalletPayload, LegacyWalletResponse
from .settings import settings


class AML:
    """AML."""

    base_url = 'https://aml-api.elliptic.co'
    auth: Auth

    def __init__(
        self,
        api_key: str = settings.api_key,
        api_secret: str = settings.api_secret,
    ):
        """Init AML class.

        Args:
            api_key: API key
            api_secret: API secret
        """
        self.auth = Auth(api_key, api_secret)

    def wallet_single_analysis(
        self,
        schema: LegacyWalletPayload,
    ) -> LegacyWalletResponse:
        """Run a single analysis.

        Args:
            schema: LegacyWalletPayload instance

        Returns:
            LegacyWalletResponse instance
        """
        payload = schema.dict()
        kwargs = {
            'method': 'POST',
            'path': '/v2/wallet/synchronous',
        }
        auth_headers = self.auth.create_headers(
            **kwargs,
            payload=payload,
        )
        response_dict = self._make_request(
            **kwargs,
            headers=auth_headers,
            json=payload,
        )
        return LegacyWalletResponse(**response_dict)

    def _make_request(self, path: str, **kwargs) -> dict:
        client = get_client()
        url = f'{self.base_url}{path}'
        response = client.request(url=url, **kwargs)
        response.raise_for_status()
        return response.json()
