from dataclasses import dataclass

from .base import Method
from ..types import QRCodeResponse


@dataclass
class GenerateQRWallet(Method[QRCodeResponse]):
    __returning__ = QRCodeResponse
    __api_method__ = "v1/wallet/qr"
    __http_method__ = "post"

    wallet_address_uuid: str


@dataclass
class GenerateQRMerchant(Method[QRCodeResponse]):
    __returning__ = QRCodeResponse
    __api_method__ = "v1/payment/qr"
    __http_method__ = "post"

    merchant_payment_uuid: str