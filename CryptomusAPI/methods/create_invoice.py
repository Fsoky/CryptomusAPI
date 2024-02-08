from dataclasses import dataclass

from .base import Method
from ..types import PaymentInfoResponse


@dataclass
class CreateInvoice(Method[PaymentInfoResponse]):
    __returning__ = PaymentInfoResponse
    __api_method__ = "v1/payment"
    __http_method__ = "post"

    amount: int | float | str
    currency: str
    order_id: str
    lifetime: int
    network: str | None = None
    url_return: str | None = None
    url_success: str | None = None
    url_callback: str | None = None
    is_payment_multiple: bool = True
    to_currency: str | None = None
    subtract: int = 0
    accuracy_payment_percent: int = 0
    additional_data: str | None = None
    currencies: list[str] | None = None
    except_currencies: list[str] | None = None
    course_source: str | None = None
    from_referral_code: str | None = None
    discount_percent: int | None = None
    is_refresh: bool = False
