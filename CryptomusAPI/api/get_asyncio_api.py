from typing import Any, Literal

from CryptomusAPI.utils.base import _BaseCryptomusPay
from CryptomusAPI.utils.models import Invoice, Wallet, QRCode
from CryptomusAPI.exceptions import CryptomusError
from CryptomusAPI.enums import *


class _CryptomusPayments(_BaseCryptomusPay):

    async def create_invoice(
        self,
        amount: int | float | str,
        currency: str | FiatCurrency | CryptoCurrency,
        order_id: str,
        *,
        network: str | BlockChain | None=None,
        url_return: str | None=None,
        url_success: str | None=None,
        url_callback: str | None=None,
        is_payment_multiple: bool=True,
        lifetime: int=3600,
        to_currency: str | CryptoCurrency | None=None,
        subtract: int=0,
        accuracy_payment_percent: int=0,
        additional_data: str | None=None,
        currencies: list[str] | list[CryptoCurrency] | None=None,
        except_currencies: list[str] | list[CryptoCurrency] | None=None,
        course_source: str | None=None,
        from_referral_code: str | None=None,
        discount_percent: int | None=None,
        is_refresh: bool=False
    ) -> Invoice:
        """
        Creating an invoice.

        :param amount: Amount to be paid.
        :param currency: Currency code.
        :param order_id: Order ID in your system.
        :param network: Blockchain network code.

        :param url_return: Before paying, the user can click on the button on the payment
        form and return to the store page at this URL.

        :param url_success: After successful payment, the user can click
        on the button on the payment form and return to this URL.

        :param url_callback: Url to which webhooks with payment status will be sent.

        :param is_payment_multiple: Whether the user is allowed to pay the remaining amount.
        This is useful when the user has not paid the entire amount of the invoice for one transaction,
        and you want to allow him to pay up to the full amount. If you disable this feature,
        the invoice will finalize after receiving the first payment and you will receive funds to your balance.
        
        :param lifetime: The lifespan of the issued invoice (in seconds).

        :param to_currency: The parameter is used to specify the target currency for converting the invoice amount.
        When creating an invoice, you provide an amount and currency, and the API will convert that amount
        to the equivalent value in the to_currency.
            - For example, to create an invoice for 20 USD in bitcoin:
                - amount: 20
                - currency: USD
                - to_currency: BTC

        :param subtract: Percentage of the payment commission charged to the client.
            - If you have a rate of 1%, then if you create an invoice for 100 USDT with subtract =
            100 (the client pays 100% commission), the client will have to pay 101 USDT.

        :param accuracy_payment_percent: Acceptable inaccuracy in payment.
        :param additional_data: Additional information for you (not shown to the client).

        :param currencies: List of allowed currencies for payment.
        This is useful if you want to limit the list of coins that your customers can use to pay invoices.

        :param except_currencies: List of excluded currencies for payment.
        :param course_source: The service from which the exchange rates are taken for conversion in the invoice.
        :param from_referral_code: The merchant who makes the request connects to a referrer by code.

        :param discount_percent: Positive numbers:
            - Allows you to set a discount.
            To set a 5% discount for the payment, you should pass a value: 5
            - Negative numbers:
            Allows you to set custom additional commission.
            - To set an additional commission of 10% for the payment, you should pass a value: -10
            - The discount percentage when creating an invoice is taken into account
            only if the invoice has a specific cryptocurrency
    
        :param is_refresh: Using this parameter, you can update the lifetime and get a new address
        for the invoice if the lifetime has expired.
  
        Simple Usage:

        .. code-block:: python
        >>> await api.payments.create_invoice(
                amount=10,
                currency=FiatCurrency.USD, # or "USD"
                order_id="TEST-ORDER-1",
                lifetime=300
            )
        """

        currency = str(currency) \
            if isinstance(currency, FiatCurrency) \
            or isinstance(currency, CryptoCurrency) \
            else currency
        to_currency = str(to_currency) if isinstance(to_currency, CryptoCurrency) else to_currency
        network = str(network) if isinstance(network, BlockChain) else network

        match amount:
            case int() | float():
                amount = str(amount)

        # NOTE: Finalise
        currencies = [
            str(cur) for cur in currencies
            if isinstance(cur, CryptoCurrency)
        ] if currencies else None
        except_currencies = [
            str(exc_cur) for exc_cur in except_currencies
            if isinstance(except_currencies, CryptoCurrency)
        ] if except_currencies else None

        if lifetime < 300 or lifetime > 43200:
            raise CryptomusError("The lifetime of the check should be between 300 and 43200 seconds.")
        if subtract < 0 or subtract > 100:
            raise CryptomusError("The subtract of the check should be between 0 and 100 value.")
        if accuracy_payment_percent < 0 or accuracy_payment_percent > 5:
            raise CryptomusError("The accuracy_payment_percent of the check should be between 0 and 5 value.")
        if additional_data and len(additional_data) > 255:
            raise CryptomusError("The additional_data of the check should be less than 255 characters.")
        if discount_percent and (discount_percent < -99 or discount_percent > 100):
            raise CryptomusError("The discount_percent of the check should be between -99 and 100 value.")

        data = self._get_func_params(locals())
        response = await self._make_request("v1/payment", data=data)

        return Invoice.model_validate(response)

    async def info(self, uuid: str, order_id: str | None=None) -> Invoice:
        data = self._get_func_params(locals())
        response = await self._make_request("v1/payment/info", data=data)

        return Invoice.model_validate(response)

    async def create_wallet(
        self,
        currency: str,
        network: str,
        order_id: str,
        *,
        url_callback: str | None=None,
        from_referral_code: str | None=None
    ) -> Wallet:
        """
        Creating a Static wallet

        :param currency: Currency code
        :param network: Blockchain network code.
        :param order_id: Order ID in your system.
        :param url_callback: URL, to which the webhook will be sent after each top-up of the wallet.
        :param from_referral_code: The merchant who makes the request connects to a referrer by code.

        Simple Usage:

        .. code-block:: python
        >>> await api.payments.create_wallet(
                currency=CryptoCurrency.USDT, # or "USDT"
                network=BlockChain.TRON, # or "tron"
                order_id="TEST-WALLET-1"
            )
        """

        currency = str(currency) if isinstance(currency, CryptoCurrency) else currency
        network = str(network) if isinstance(network, BlockChain) else network

        data = self._get_func_params(locals())

        response = await self._make_request("v1/payment/creating-static", data=data)
        return Wallet.model_validate(response)
    
    async def qr_code(
        self,
        *,
        wallet_address_uuid: str | None=None,
        merchant_payment_uuid: str | None=None
    ) -> QRCode:
        """
        Generate a QR-code for the static wallet address
        or for the invoice address

        :param wallet_address_uuid: UUID of a static wallet
        :param merchant_payment_uuid: Invoice uuid

        Simple Usage:

        .. code-block:: python
        # Generate QR for wallet
        >>> await api.payments.qr_code(
                wallet_address_uuid="YOUR WALLET ADDRESS UUID"
            )

        # Generate QR for invoice
        >>> await api.payments.qr_code(
                merchant_payment_uuid="YOUR INVOICE UUID"
            )
        """

        payload = dict(
            endpoint="v1/payment/qr",
            data={"merchant_payment_uuid": merchant_payment_uuid}
        )

        if wallet_address_uuid:
            payload["endpoint"] = "v1/wallet/qr"
            payload["data"] = {"wallet_address_uuid": wallet_address_uuid}

        response = await self._make_request(**payload)
        return QRCode.model_validate(response)