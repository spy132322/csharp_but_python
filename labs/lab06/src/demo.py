from models import (
    Product,
    LiquidProduct,
    TangibleProduct,
    ServiceProduct
)

from container import (
    TypedCollection,
    DisplayCollection,
    ScoreCollection
)


def title(text: str) -> None:
    print(f"\n{'=' * 15} {text} {'=' * 15}")


def scenario_1() -> None:
    title("SCENARIO 1 — TYPED COLLECTION")

    products: TypedCollection[Product] = TypedCollection()

    products.add(Product("Phone", 1000, 10, 5))
    products.add(LiquidProduct("Water", 2, stock=50, volume_liters=2))
    products.add(TangibleProduct("Laptop", 2000, stock=3, weight_kg=2))
    products.add(ServiceProduct("Repair", 100, stock=10, hours=2))

    print("\nALL PRODUCTS:")

    for item in products.get_all():
        print(item)

    print("\nCOLLECTION SIZE:")
    print(products.size())

    print("\nCONTAINS PHONE:")
    print(products.contains(products.get_all()[0]))

    print("\nTYPE VALIDATION:")
    print("TypedCollection[Product] accepts only Product objects")


def scenario_2() -> None:
    title("SCENARIO 2 — FIND FILTER MAP")

    products: TypedCollection[Product] = TypedCollection()

    products.add(Product("Phone", 1000, 10, 5))
    products.add(Product("TV", 3000, 5, 2))
    products.add(ServiceProduct("Repair", 100, stock=10, hours=2))

    found = products.find(lambda p: p.name == "TV")

    print("\nFIND EXISTING:")
    print(found)

    not_found = products.find(lambda p: p.name == "Tablet")

    print("\nFIND NONE:")
    print(not_found)

    expensive = products.filter(
        lambda p: p.calculate_price() > 500
    )

    print("\nFILTER EXPENSIVE:")

    for item in expensive:
        print(item)

    names: list[str] = products.map(lambda p: p.name)

    print("\nMAP TO list[str]:")
    print(names)

    prices: list[float] = products.map(
        lambda p: p.calculate_price()
    )

    print("\nMAP TO list[float]:")
    print(prices)


def scenario_3() -> None:
    title("SCENARIO 3 — PROTOCOLS")

    display_items: DisplayCollection[Product] = DisplayCollection()

    display_items.add(Product("Phone", 1000))
    display_items.add(LiquidProduct("Milk", 3, volume_liters=1.5))
    display_items.add(ServiceProduct("Cleaning", 50, hours=3))

    print("\nDISPLAYABLE PROTOCOL:")

    display_items.show()

    score_items: ScoreCollection[Product] = ScoreCollection()

    score_items.add(Product("Phone", 1000))
    score_items.add(TangibleProduct("Table", 300, weight_kg=10))
    score_items.add(ServiceProduct("Consulting", 200, hours=2))

    print("\nSCORABLE PROTOCOL:")

    score_items.show_scores()

    print("\nPROTOCOL CHECK:")
    print("Classes work without explicit inheritance from Protocol")


def main() -> None:
    scenario_1()
    scenario_2()
    scenario_3()


if __name__ == "__main__":
    main()
