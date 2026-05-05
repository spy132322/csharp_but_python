from interfaces import Printable, Comparable


class Product(Printable, Comparable):
    def __init__(self, name, price, discount=0.0, stock=0, active=True):
        self.name = name
        self.price = price
        self.discount = discount
        self.stock = stock
        self.active = active

    def price_after_discount(self):
        return round(self.price * (1 - self.discount / 100), 2)

    def calculate_price(self):
        return self.price_after_discount()

    def activate(self):
        self.active = True

    def to_string(self) -> str:
        return str(self)

    def compare_to(self, other: object) -> int:
        if not isinstance(other, Product):
            raise TypeError
        a = self.calculate_price()
        b = other.calculate_price()
        return (a > b) - (a < b)

    def __str__(self):
        return (
            f"{self.name} | base | price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | active: {self.active}"
        )


class LiquidProduct(Product):
    def __init__(self, name, price, discount=0.0, stock=0, active=True, volume_liters=1.0, bottle_fee=0.0):
        super().__init__(name, price, discount, stock, active)
        self._volume_liters = volume_liters
        self._bottle_fee = bottle_fee

    def calculate_price(self):
        return round(self.price_after_discount() * self._volume_liters + self._bottle_fee, 2)

    def __str__(self):
        return (
            f"{self.name} | liquid | volume: {self._volume_liters:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )


class TangibleProduct(Product):
    def __init__(self, name, price, discount=0.0, stock=0, active=True, weight_kg=1.0, logistics_fee=0.0):
        super().__init__(name, price, discount, stock, active)
        self._weight_kg = weight_kg
        self._logistics_fee = logistics_fee

    def calculate_price(self):
        return round(self.price_after_discount() + self._weight_kg * self._logistics_fee, 2)

    def __str__(self):
        return (
            f"{self.name} | tangible | weight: {self._weight_kg:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )


class ServiceProduct(Product):
    def __init__(self, name, price, discount=0.0, stock=0, active=True, hours=1.0, complexity=1.0):
        super().__init__(name, price, discount, stock, active)
        self._hours = hours
        self._complexity = complexity

    def calculate_price(self):
        return round(self.price_after_discount() * self._hours * self._complexity, 2)

    def __str__(self):
        return (
            f"{self.name} | service | hours: {self._hours:.2f} | "
            f"price: {self.calculate_price():.2f} | stock: {self.stock} | active: {self.active}"
        )
