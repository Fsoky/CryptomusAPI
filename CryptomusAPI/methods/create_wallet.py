from dataclasses import dataclass

from .base import Method
from ..types import WalletResponse, BlockWalletResponse, RefundBlockedResponse


@dataclass
class CreateWallet(Method[WalletResponse]):
    __returning__ = WalletResponse
    __api_method__ = "v1/wallet/creating-static"
    __http_method__ = "post"

    currency: str
    network: str
    order_id: str
    url_callback: str | None = None
    from_referral_code: str | None = None


@dataclass
class BlockWallet(Method[BlockWalletResponse]):
    __returning__ = WalletResponse
    __api_method__ = "v1/wallet/block-address"
    __http_method__ = "post"

    uuid: str
    order_id: str
    is_force_refund: bool = False


@dataclass
class RefundBlocked(Method[RefundBlockedResponse]):
    __returning__ = RefundBlockedResponse
    __api_method__ = "v1/wallet/blocked-address-refund"
    __http_method__ = "post"

    address: str
    uuid: str | None = None
    order_id: str | None = None