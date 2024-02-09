from dataclasses import dataclass

from .base import Method
from ..types import RefundResponse


@dataclass
class Refund(Method[RefundResponse]):
    __returning__ = RefundResponse
    __api_method__ = "v1/payment/refund"
    __http_method__ = "post"

    address: str
    is_subtract: bool
    uuid: str | None = None
    order_id: str | None = None