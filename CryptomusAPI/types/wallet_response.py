from __future__ import annotations
from dataclasses import dataclass
from typing import Any


@dataclass
class WalletResponse:
    wallet_uuid: str
    uuid: str
    address: str
    network: str
    currency: str
    url: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> WalletResponse:
        return cls(state=data["state"], **data["result"])
    

@dataclass
class BlockWalletResponse:
    state: int
    uuid: str
    status: str

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> BlockWalletResponse:
        return cls(state=data["state"], **data["result"])
    

@dataclass
class RefundBlockedResponse:
    state: int
    commission: float
    amount: float

    @classmethod
    def from_json(cls, data: dict[str, Any]) -> RefundBlockedResponse:
        return cls(state=data["state"], **data["result"])