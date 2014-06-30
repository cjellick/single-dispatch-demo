from demo.payment_types import *


class PaymentHandler(object):
    """
    This class is an example of the 'old' way of doing things:
    a factory method that makes some specfic if/elif/els tests to determine which
    handler to return.
    """

    def process(self, payment, shipping_address):
        print("Not implemented. You need to manually process [%s] for [%s]" % (
            payment, shipping_address))

    @staticmethod
    def get_handler(payment):
        if isinstance(payment, CreditCardPayment):
            handler_cls = CreditCardPaymentHandler
        elif isinstance(payment, OfflinePayment):
            if isinstance(payment, CODPayment):
                handler_cls = CODPaymentHandler
            else:
                handler_cls = OfflinePaymentHandler
        else:
            handler_cls = PaymentHandler

        handler = handler_cls()
        return handler


class CreditCardPaymentHandler(PaymentHandler):
    def process(self, payment, shipping_address):
        print('Doing credit card processing.')


class OfflinePaymentHandler(PaymentHandler):
    def process(self, payment, shipping_address):
        print('Offline payment. Did you get your money?')


class CODPaymentHandler(PaymentHandler):
    def process(self, payment, shipping_address):
        print('COD payment. Better ship your order!')


