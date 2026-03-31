# lab01/model.py
from lab01.src.validators import _validate_name, _validate_price, _validate_discount, _validate_stock

class Product:
    TAX_RATE = 0.20

    def __init__(self, name, price, discount=0.0, stock=0, active=True):
        self._name = _validate_name(name)
        self._price = _validate_price(price)
        self._discount = _validate_discount(discount)
        self._stock = _validate_stock(stock)
        self._active = bool(active)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = _validate_price(value)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        self._discount = _validate_discount(value)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        self._stock = _validate_stock(value)

    @property
    def active(self):
        return self._active

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def price_after_discount(self):
        return round(self._price * (1 - self._discount / 100), 2)

    def price_with_tax(self):
        return round(self.price_after_discount() * (1 + Product.TAX_RATE), 2)

    def purchase(self, quantity):
        if not isinstance(quantity, int):
            raise TypeError("quantity must be int")
        if quantity <= 0:
            raise ValueError("quantity must be > 0")
        if not self._active:
            raise RuntimeError("cannot purchase inactive product")
        if quantity > self._stock:
            raise ValueError("not enough stock")
        self._stock -= quantity
        total = round(quantity * self.price_after_discount(), 2)
        return total

    def restock(self, amount):
        if not isinstance(amount, int):
            raise TypeError("restock amount must be int")
        if amount <= 0:
            raise ValueError("restock amount must be > 0")
        self._stock += amount

    def __str__(self):
        return f"{self._name} | price: {self.price_after_discount():.2f} | tax price: {self.price_with_tax():.2f} | discount: {self._discount:.1f}% | stock: {self._stock} | active: {self._active}"

    def __repr__(self):
        return f"Product(name={self._name!r}, price={self._price!r}, discount={self._discount!r}, stock={self._stock!r}, active={self._active!r})"

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return (self._name == other._name and
                abs(self._price - other._price) < 1e-9 and
                abs(self._discount - other._discount) < 1e-9 and
                self._stock == other._stock and
                self._active == other._active)
