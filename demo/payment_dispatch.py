from functools import singledispatch
from demo.payment_types import *


@singledispatch
def process_payment(payment, shipping_address):
    """
    Decorated with @singledispatch, so calls to this function will
    dispatch to one of the handlers registered below. If none is found,
    it will fall back to this method.
    """
    print("Not implemented. You need to manually process [%s] for [%s]" % (
        payment, shipping_address))


@process_payment.register(CreditCardPayment)
def credit_card(payment, shipping_address):
    print('Doing electronic processing.')


@process_payment.register(OfflinePayment)
def offline(payment, shipping_address):
    print('Offline payment. Did you get your money?')


@process_payment.register(CODPayment)
def cod_process(payment, shipping_address):
    print('COD payment. Better ship your order!')
