from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass
class PaymentInfoResponse:
    state: int
    uuid: str
    order_id: str
    amount: float
    payment_status: str
    url: str
    expired_at: int
    status: str
    is_final: bool
    created_at: datetime
    updated_at: datetime
    commission: float
    payment_amount: float | None = None
    payment_amount_usd: float | None = None
    payer_amount: float | None = None
    additional_data: str | None = None
    payer_amount_exchange_rate: float | None = None
    discount_percent: float | None = None
    discount: float | None = None
    payer_currency: str | None = None
    currency: str | None = None
    comments: str | None = None
    merchant_amount: float | None = None
    network: str | None = None
    address: str | None = None
    from_: str | None = None
    txid: str | None = None

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> PaymentInfoResponse:
        from_ = data["result"].pop("from", None)
        return cls(state=data["state"], from_=from_, **data["result"])