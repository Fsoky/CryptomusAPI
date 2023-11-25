from typing import Any
from pydantic import BaseModel

from datetime import datetime


class BaseCryptomusResponse(BaseModel):
    state: int


class InvoiceResult(BaseModel):
    uuid: str
    order_id: str
    amount: float
    payment_amount: float | None = None
    payment_amount_usd: float | None = None
    payer_amount: float | None = None
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
    payment_status: str
    url: str
    expired_at: int
    status: str
    is_final: bool
    additional_data: str | None = None
    created_at: datetime
    updated_at: datetime


class WalletResult(BaseModel):
    wallet_uuid: str
    uuid: str
    address: str
    network: str
    currency: str
    url: str


class Invoice(BaseCryptomusResponse):
    result: InvoiceResult


class Wallet(BaseCryptomusResponse):
    result: WalletResult


class QRCode(BaseCryptomusResponse):
    image: str