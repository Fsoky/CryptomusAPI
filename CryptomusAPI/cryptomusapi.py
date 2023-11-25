from .utils.base import _BaseCryptomusPay
from .api.get_asyncio_api import _CryptomusPayments


class Cryptomus(_BaseCryptomusPay):
    
    @property
    def payments(self) -> _CryptomusPayments:
        return _CryptomusPayments(self._merchant_uuid, self._api_key)