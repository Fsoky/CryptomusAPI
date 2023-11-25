class CryptomusError(Exception):

    def __init__(self, message: str) -> None:
        return super().__init__(message)