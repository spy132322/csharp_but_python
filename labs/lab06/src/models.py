from interfaces import Printable, Comparable


class Product(Printable, Comparable):
    def __init__(
        self,
        name: str,
        price: float,
        discount: float = 0.0,
        stock: int = 0,
        active: bool = True
    ) -> None:
        self.name: str = name
        self.price: float = price
        self.discount: float = discount
        self.stock: int = stock
        self.active: bool = active

    def price_after_discount(self) -> float:
        return round(self.price * (1 - self.discount / 100), 2)

    def calculate_price(self) -> float:
        return self.price_after_discount()

    def activate(self) -> None:
        self.active = True

    def to_string(self) -> str:
        return str(self)

    def display(self) -> str:
        return str(self)

    def score(self) -> float:
        return self.calculate_price()

    def compare_to(self, other: object) -> int:
        if not isinstance(other, Product):
            raise TypeError

        a: float = self.calculate_price()
        b: float = other.calculate_price()

        return (a > b) - (a < b)

    def __str__(self) -> str:
        return (
            f"{self.name} | base | "
            f"price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | "
            f"active: {self.active}"
        )


class LiquidProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        discount: float = 0.0,
        stock: int = 0,
        active: bool = True,
        volume_liters: float = 1.0,
        bottle_fee: float = 0.0
    ) -> None:
        super().__init__(name, price, discount, stock, active)

        self._volume_liters: float = volume_liters
        self._bottle_fee: float = bottle_fee

    def calculate_price(self) -> float:
        return round(
            self.price_after_discount() * self._volume_liters + self._bottle_fee,
            2
        )

    def __str__(self) -> str:
        return (
            f"{self.name} | liquid | "
            f"volume: {self._volume_liters:.2f} | "
            f"price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | "
            f"active: {self.active}"
        )


class TangibleProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        discount: float = 0.0,
        stock: int = 0,
        active: bool = True,
        weight_kg: float = 1.0,
        logistics_fee: float = 0.0
    ) -> None:
        super().__init__(name, price, discount, stock, active)

        self._weight_kg: float = weight_kg
        self._logistics_fee: float = logistics_fee

    def calculate_price(self) -> float:
        return round(
            self.price_after_discount() + self._weight_kg * self._logistics_fee,
            2
        )

    def __str__(self) -> str:
        return (
            f"{self.name} | tangible | "
            f"weight: {self._weight_kg:.2f} | "
            f"price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | "
            f"active: {self.active}"
        )


class ServiceProduct(Product):
    def __init__(
        self,
        name: str,
        price: float,
        discount: float = 0.0,
        stock: int = 0,
        active: bool = True,
        hours: float = 1.0,
        complexity: float = 1.0
    ) -> None:
        super().__init__(name, price, discount, stock, active)

        self._hours: float = hours
        self._complexity: float = complexity

    def calculate_price(self) -> float:
        return round(
            self.price_after_discount() * self._hours * self._complexity,
            2
        )

    def __str__(self) -> str:
        return (
            f"{self.name} | service | "
            f"hours: {self._hours:.2f} | "
            f"price: {self.calculate_price():.2f} | "
            f"stock: {self.stock} | "
            f"active: {self.active}"
        )
