from typing import Any, Literal

from .session.base import BaseSession
from .session._aiohttp import AIOHTTPSession

from CryptomusAPI.methods import *
from CryptomusAPI.types import *


class CryptomusClient:

    def __init__(
        self,
        merchant_id: str,
        api_key: str,
        session: BaseSession | None = None
    ) -> None:
        _session = session or AIOHTTPSession(api_key)
        _session.headers["merchant"] = merchant_id
        self.session = _session

    @staticmethod
    def __get_func_params(params: dict[str, Any]) -> dict[str, Any]:
        if params.get("self"): del params["self"]
        return {
            k: v for k, v in params.items()
            if v is not None
        }

    async def get_payment_info(
        self, uuid: str, order_id: str | None = None
    ) -> PaymentInfoResponse:
        return await self.session(GetPaymentInfo(uuid, order_id))
    
    async def create_invoice(
        self,
        amount: int | float | str,
        currency: str,
        order_id: str,
        *,
        network: str | None = None,
        url_return: str | None = None,
        url_success: str | None = None,
        url_callback: str | None = None,
        is_payment_multiple: bool = True,
        lifetime: int = 3600,
        to_currency: str | None = None,
        subtract: int = 0,
        accuracy_payment_percent: int = 0,
        additional_data: str | None = None,
        currencies: list[str] | None = None,
        except_currencies: list[str] | None = None,
        course_source: str | None = None,
        from_referral_code: str | None = None,
        discount_percent: int | None = None,
        is_refresh: bool = False
    ) -> PaymentInfoResponse:
        if not isinstance(amount, str):
            amount = str(amount)

        return await self.session(CreateInvoice(**self.__get_func_params(locals())))
    
    async def create_wallet(
        self,
        currency: str,
        network: str,
        order_id: str,
        *,
        url_callback: str | None = None,
        from_referral_code: str | None = None
    ) -> WalletResponse:
        return await self.session(CreateWallet(**self.__get_func_params(locals())))
    
    async def block_wallet(
        self, uuid: str, order_id: str, is_force_refund: bool = False
    ) -> BlockWalletResponse:
        return await self.session(BlockWallet(uuid, order_id, is_force_refund))
    
    async def generate_qr(
        self, uuid: str, for_what: Literal["wallet", "merchant"] = "wallet"
    ) -> QRCodeResponse:
        request = GenerateQRWallet(uuid) if for_what == "wallet" else GenerateQRMerchant(uuid)
        return await self.session(request)
    
    async def blocked_address_refund(
        self, address: str, *, uuid: str | None = None, order_id: str | None = None
    ) -> RefundBlockedResponse:
        return await self.session(RefundBlockedResponse(address, uuid, order_id))
    
    async def refund(
        self, address: str, is_subtract: bool, uuid: str | None = None, order_id: str | None = None
    ) -> RefundResponse:
        return await self.session(Refund(address, is_subtract, uuid, order_id))