"""Elliptic SDK elliptic_sdk/auth.py."""
import base64
import hashlib
import hmac as crypto
import json
import time


class Auth:
    """Auth."""

    _api_key: str
    _api_secret: str

    def __init__(self, api_key: str, api_secret: str):
        """Init Auth class.

        Args:
            api_key: API key
            api_secret: API secret
        """
        self._api_key = api_key
        self._api_secret = api_secret

    def create_headers(
        self,
        method: str,
        path: str,
        payload: dict = None,
    ):
        """Create auth headers.

        https://developers.elliptic.co/docs/authentication

        Args:
            method: Uppercase method name
            path: API endpoint including query string
            payload: String encoded dict or None if there is no request body

        Returns:
            dict of Auth headers
        """
        timestamp = str(int(round(time.time() * 1000)))
        payload_json = json.dumps(
            payload,
            separators=(',', ':'),
        )
        sign = self._sign_request(
            timestamp,
            method=method,
            path=path,
            payload=payload_json,
        )
        return {
            'x-access-key': self._api_key,
            'x-access-sign': sign,
            'x-access-timestamp': timestamp,
        }

    def _sign_request(
        self,
        timestamp: str,
        *,
        method,
        path,
        payload=None,
    ):
        if payload is None:
            payload = {}
        hmac = crypto.new(
            base64.b64decode(self._api_secret),
            digestmod=hashlib.sha256,
        )
        request_text = ''.join(
            [
                timestamp,
                method,
                path.lower(),
                payload,
            ],
        )
        hmac.update(request_text.encode('utf-8'))
        return base64.b64encode(hmac.digest()).decode('utf-8')
