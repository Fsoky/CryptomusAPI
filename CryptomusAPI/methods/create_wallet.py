from dataclasses import dataclass

from .base import Method
from ..types import WalletResponse


@dataclass
class CreateWallet(Method[WalletResponse]):
    __returning__ = WalletResponse
    __api_method__ = "v1/payment/creating-static"
    __http_method__ = "post"

    currency: str
    network: str
    order_id: str
    url_callback: str | None = None
    from_referral_code: str | None = None