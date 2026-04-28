from __future__ import annotations

from .interfaces import Comparable, Printable
from .models import LiquidProduct, Product, ServiceProduct, TangibleProduct
from lab03.src.collection import ProductCatalog


def print_all(items: list[Printable]) -> None:
    print("\n--- PRINT ALL (Printable) ---")
    for item in items:
        print(item.to_string())


def compare_demo(left: Comparable, right: Comparable, title: str) -> None:
    print(f"\n--- {title} ---")
    print(f"{left.__class__.__name__} compare_to {right.__class__.__name__}: {left.compare_to(right)}")


def dump(title: str, items) -> None:
    print(f"\n--- {title} ---")
    for item in items:
        print(item)


def scenario_1_polymorphism_and_interfaces() -> None:
    water = LiquidProduct("Вода", 40, 5, stock=12, volume_liters=1.5, bottle_fee=3)
    bolt = TangibleProduct("Болт", 15, 0, stock=200, weight_kg=0.08, logistics_fee=18)
    hole = ServiceProduct("Яма", 2500, 10, stock=2, hours=3, complexity=1.4)

    items: list[Product] = [water, bolt, hole]

    dump("RAW OBJECTS", items)

    print_all(items)

    print("\n--- isinstance ---")
    for item in items:
        print(
            f"{item.name}: "
            f"Printable={isinstance(item, Printable)}, "
            f"Comparable={isinstance(item, Comparable)}, "
            f"Product={isinstance(item, Product)}"
        )

    compare_demo(water, bolt, "COMPARE WATER VS BOLT")
    compare_demo(hole, water, "COMPARE HOLE VS WATER")


def scenario_2_catalog_and_filtering() -> None:
    catalog = ProductCatalog(
        [
            LiquidProduct("Сок", 120, 10, stock=7, volume_liters=1.0, bottle_fee=6),
            TangibleProduct("Гвоздь", 8, 0, stock=500, weight_kg=0.02, logistics_fee=25),
            ServiceProduct("Яма", 3000, 0, stock=1, hours=4, complexity=1.2),
            LiquidProduct("Молоко", 90, 3, stock=15, volume_liters=0.9, bottle_fee=4),
        ]
    )

    dump("ALL CATALOG ITEMS", catalog)

    printable = catalog.get_printable()
    comparable = catalog.get_comparable()

    dump("PRINTABLE ITEMS", printable)
    dump("COMPARABLE ITEMS", comparable)

    catalog.sort_by_comparable()
    dump("SORTED BY COMPARABLE", catalog)


def scenario_3_collection_behavior() -> None:
    catalog = ProductCatalog(
        [
            LiquidProduct("Вода", 40, 5, stock=12, volume_liters=1.5, bottle_fee=3),
            TangibleProduct("Болт", 15, 0, stock=200, weight_kg=0.08, logistics_fee=18),
            ServiceProduct("Яма", 2500, 10, stock=2, hours=3, complexity=1.4),
            ServiceProduct("Траншея", 1800, 0, stock=1, hours=5, complexity=1.1),
        ]
    )

    dump("INITIAL", catalog)

    active = catalog.get_active()
    available = catalog.get_available()
    expensive = catalog.get_expensive(200)

    dump("ACTIVE", active)
    dump("AVAILABLE", available)
    dump("EXPENSIVE >= 200", expensive)

    service = catalog.find_by_name("Яма")
    print("\n--- PURCHASE BEFORE ---")
    print(service)

    if isinstance(service, ServiceProduct):
        service.purchase(1)

    print("\n--- PURCHASE AFTER ---")
    print(service)

    catalog.sort_by_price()
    dump("SORTED BY PRICE", catalog)


def main() -> None:
    scenario_1_polymorphism_and_interfaces()
    scenario_2_catalog_and_filtering()
    scenario_3_collection_behavior()


if __name__ == "__main__":
    main()