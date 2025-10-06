from __future__ import annotations
from typing import Callable, Any
from types import TracebackType
from abc import ABC, abstractmethod
import json

from adaptix.load_error import LoadError

from CryptomusAPI.methods.base import Method, ResponseType
from CryptomusAPI.exceptions import CryptomusError

_JsonDumps = Callable[..., Any]

DEFAULT_TIMEOUT = 60.0
DEFAULT_HEADERS = {
    "merchant": "",
    "sign": "",
    "Content-Type": "application/json"
}
API_BASE_URL = "https://api.cryptomus.com/{}"


class BaseSession(ABC):

    def __init__(
        self,
        json_dumps: _JsonDumps = json.dumps,
        timeout: float = DEFAULT_TIMEOUT,
        headers: dict[str, str] | None = None,
        api_endpoint: str | None = None
    ) -> None:
        self.json_dumps = json_dumps
        self.timeout = timeout
        self.headers = headers or DEFAULT_HEADERS
        self.endpoint = api_endpoint or API_BASE_URL

    def check_response(
        self,
        method: Method[ResponseType],
        status_code: int,
        data: dict[str, Any]
    ) -> ResponseType:
        try:
            json_data = self.json_dumps(data)
        except Exception as e:
            raise CryptomusError(f"Error while parsing json: {e}")

        if status_code == 200:
            try:
                obj = method.build_response(json_data)
            except LoadError as e:
                raise CryptomusError(f"Error while building response: {e}")
            return obj

        raise CryptomusError(f"Error while request [{status_code}]: {json_data}")
    
    @abstractmethod
    async def make_request(self, method: Method[ResponseType]) -> ResponseType:
        ...

    @abstractmethod
    async def close(self) -> None:
        ...
    
    async def __aenter__(self) -> BaseSession:
        return self
    
    async def __aexit__(
        self,
        exc_type: type[BaseException],
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.close()

    async def __call__(self, method: Method[ResponseType]) -> ResponseType:
        return await self.make_request(method)