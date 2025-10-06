import base64
import hashlib

from aiohttp import ClientSession

from .base import BaseSession
from CryptomusAPI.methods.base import Method, ResponseType

API_BASE_URL = "https://api.cryptomus.com/{}"


class AIOHTTPSession(BaseSession):

    def __init__(self, __api_key: str):
        self.__api_key = __api_key
        self.session: ClientSession | None = None
        super().__init__()

    async def __aenter__(self) -> BaseSession:
        await self._get_session()
        return await super().__aenter__()

    async def _get_session(self) -> ClientSession:
        if self.session is None or self.session.closed:
            self.session = ClientSession()
        return self.session

    async def make_request(self, method: Method[ResponseType]) -> ResponseType:
        session = await self._get_session()

        url = API_BASE_URL.format(method.__api_method__)
        data = method.to_str() or ""
        sign = hashlib.md5(
            base64.b64encode(data.encode('ascii')) + self.__api_key.encode('ascii')
        ).hexdigest()

        self.headers["sign"] = sign
        async with session.request(
            method.__http_method__,
            url,
            headers=self.headers,
            data=method.to_str(),
            timeout=self.timeout
        ) as response:
            return self.check_response(method, response.status, await response.json())
    
    async def close(self) -> None:
        if self.session and not self.session.closed:
            await self.session.close()