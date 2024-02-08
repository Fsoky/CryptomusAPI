from dataclasses import dataclass

from .base import Method
from ..types import PaymentInfoResponse


@dataclass
class GetPaymentInfo(Method[PaymentInfoResponse]):
    __returning__ = PaymentInfoResponse
    __api_method__ = "v1/payment/info"
    __http_method__ = "post"

    uuid: str
    order_id: str | None = None