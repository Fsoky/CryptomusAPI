from .base_enum import _BaseCryptomusEnum


class PaymentStatus(_BaseCryptomusEnum):
    """
    The payment status comes in the response body of some methods
    and indicates at what stage the payment is at the moment.
    """

    PAID = "paid"
    PAID_OVER = "paid_over"
    WRONG_AMOUNT = "wrong_amount"
    PROCESS = "process"
    CONFIRM_CHECK = "confirm_check"
    WRONG_AMOUNT_WAITING = "wrong_amount_waiting"
    CHECK = "check"
    FAIL = "fail"
    CANCEL = "cancel"
    SYSTEM_FAIL = "system_fail"
    REFUND_PROCESS = "refund_process"
    REFUND_FAIL = "refund_fail"
    REFUND_PAID = "refund_paid"
    LOCKED = "locked"