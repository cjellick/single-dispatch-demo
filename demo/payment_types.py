class AbstractPayment(object):
    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return str(self.amount)


class PayPalPayment(AbstractPayment):
    pass


class CreditCardPayment(AbstractPayment):
    pass


class OfflinePayment(AbstractPayment):
    pass


class CODPayment(OfflinePayment):
    pass


class PhonePayment(OfflinePayment):
    pass


class ShippingAddress(object):
    def __init__(self, address):
        self.address = address

    def __str__(self):
        return self.address