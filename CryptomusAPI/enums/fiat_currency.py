from .base_enum import _BaseCryptomusEnum


class FiatCurrency(_BaseCryptomusEnum):
    """
    Listing of available fiat currencies.
    """

    USD = "USD"
    EUR = "EUR"
    RUB = "RUB"