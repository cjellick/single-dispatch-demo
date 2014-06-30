from demo.payment_types import *
from demo.payment_dispatch import *
from demo.payment_handlers import *


def main():
    # A little setup first
    shipping_address = ShippingAddress('123 Test St. Phoenix, AZ 85022')
    payment = PayPalPayment(1)

    # Calling the single-dispatch function
    process_payment(payment, shipping_address)

    # Doing the same with a different payment type
    payment = CreditCardPayment(2)
    process_payment(payment, shipping_address)

    # For comparison, using a traditional factory method/handler pattern
    handler = PaymentHandler.get_handler(payment)
    handler.process(payment, shipping_address)

if __name__ == '__main__':
    main()
