from __future__ import annotations

from collection import ProductCatalog
from base import Product
from models import LiquidProduct, ServiceProduct, TangibleProduct


def dump(title, items):
    print(f"\n--- {title} ---")
    for item in items:
        print(item)


def scenario_one():
    water = LiquidProduct("Вода", 40, 5, stock=12, volume_liters=1.5, bottle_fee=3)
    bolt = TangibleProduct("Болт", 15, 0, stock=200, weight_kg=0.08, logistics_fee=18)
    hole = ServiceProduct("Яма", 2500, 10, stock=2, hours=3, complexity=1.4)

    items = [water, bolt, hole]

    dump("BEFORE", items)

    water.dilute(0.5)
    bolt.add_packaging(2)
    hole.extend_duration(1)

    dump("AFTER", items)

    for item in items:
        print(type(item).__name__, isinstance(item, Product), item.calculate_price())


def scenario_two():
    catalog = ProductCatalog(
        [
            LiquidProduct("Сок", 120, 10, stock=7, volume_liters=1.0, bottle_fee=6),
            TangibleProduct("Гвоздь", 8, 0, stock=500, weight_kg=0.02, logistics_fee=25),
            ServiceProduct("Яма", 3000, 0, stock=1, hours=4, complexity=1.2),
            LiquidProduct("Молоко", 90, 3, stock=15, volume_liters=0.9, bottle_fee=4),
        ]
    )

    dump("BEFORE SORT", catalog)

    catalog.sort_by_price()

    dump("AFTER SORT BY PRICE", catalog)

    expensive = catalog.get_expensive(200)
    dump("EXPENSIVE >= 200", expensive)


def scenario_three():
    catalog = ProductCatalog(
        [
            LiquidProduct("Вода", 40, 5, stock=12, volume_liters=1.5, bottle_fee=3),
            TangibleProduct("Болт", 15, 0, stock=200, weight_kg=0.08, logistics_fee=18),
            ServiceProduct("Яма", 2500, 10, stock=2, hours=3, complexity=1.4),
            ServiceProduct("Траншея", 1800, 0, stock=1, hours=5, complexity=1.1),
        ]
    )

    dump("ALL", catalog)

    only_liquid = catalog.get_only_liquid()
    only_tangible = catalog.get_only_tangible()
    only_service = catalog.get_only_service()

    dump("ONLY LIQUID", only_liquid)
    dump("ONLY TANGIBLE", only_tangible)
    dump("ONLY SERVICE", only_service)

    service = catalog.find_by_name("Яма")

    print("\n--- PURCHASE BEFORE ---")
    print(service)

    if isinstance(service, ServiceProduct):
        service.purchase(1)

    print("\n--- PURCHASE AFTER ---")
    print(service)


def main():
    scenario_one()
    scenario_two()
    scenario_three()


if __name__ == "__main__":
    main()