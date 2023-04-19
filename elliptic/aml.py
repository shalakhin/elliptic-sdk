import json
import time
import base64
import hashlib
# import httpx
import requests
import hmac as crypto
from .settings import settings
from .schemas import LegacyWalletPayload
from .schemas import LegacyWalletResponse


class AML:
    ROOT = 'https://aml-api.elliptic.co'

    def __init__(self,
                 api_key: str = settings.api_key,
                 api_secret: str = settings.api_secret
                 ):
        self.api_key = api_key
        self.api_secret = api_secret

    @staticmethod
    def timestamp() -> str:
        return str(int(round(time.time() * 1000)))

    @staticmethod
    def sign(secret, time_of_request, http_method, http_path, payload) -> str:
        hmac = crypto.new(base64.b64decode(secret), digestmod=hashlib.sha256)
        request_text = ''.join([
            time_of_request,
            http_method,
            http_path.lower(),
            payload
        ])
        hmac.update(request_text.encode('UTF-8'))
        return base64.b64encode(hmac.digest()).decode('utf-8')

    def legacy_wallet(
            self, payload: LegacyWalletPayload) -> LegacyWalletResponse:
        url = "/v2/wallet/synchronous"
        timestamp = self.timestamp()
        signature = self.sign(settings.api_secret, timestamp, 'POST', url,
                              json.dumps(payload.dict(),
                                         separators=(',', ':')))
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            'x-access-key': self.api_key,
            'x-access-sign': signature,
            'x-access-timestamp': timestamp
        }
        full_path = f'{self.ROOT}{url}'
        response = requests.post(full_path, json=payload.dict(),
                                 headers=headers)
        return LegacyWalletResponse(**response.json())
