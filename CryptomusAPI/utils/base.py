from typing_extensions import Self
from typing import Literal, Any

import hashlib
import base64
import json

import aiohttp

from CryptomusAPI.exceptions import CryptomusError


class _BaseCryptomusPay:
    _BASE_API_LINK = "https://api.cryptomus.com/"

    def __init__(self, merchant_uuid: str, api_key: str) -> None:
        self._merchant_uuid = merchant_uuid
        self._api_key = api_key

    async def __aenter__(self) -> Self:
        return self
    
    async def __aexit__(self, exc_type, exc_value, traceback) -> None:
        return None
    
    async def _make_request(self, endpoint: str, method: Literal["post", "get"]="post", **kwargs) -> Any:
        json_dumps = json.dumps(kwargs["data"])
        sign = hashlib.md5(
            base64.b64encode(json_dumps.encode('ascii')) + self._api_key.encode('ascii')
        ).hexdigest()

        headers = {
            "merchant": self._merchant_uuid,
            "sign": sign,
            "Content-Type": "applicaiton/json"
        }

        async with aiohttp.ClientSession(headers=headers) as session:
            response = await session.request(method, f"{self._BASE_API_LINK}{endpoint}", data=json_dumps)

            match response.status:
                case 405:
                    raise CryptomusError("[405] Method not allowed")

            data = await response.json()
            print(data)
            if data.get("message"):
                raise CryptomusError(data["message"])
            if data.get("errors"):
                raise CryptomusError(str(data["errors"]))
            return data

    @staticmethod
    def _get_func_params(params: dict[str, Any]) -> dict[str, Any]:
        if params.get("self"):
            del params["self"]

        data = {}
        [
            data.update({key: value})
            for key, value in params.items()
            if params[key] is not None
        ]

        return data