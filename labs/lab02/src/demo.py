from pathlib import Path
import sys

if __package__ is None or __package__ == "":
    sys.path.append(str(Path(__file__).resolve().parents[1]))

from lab01.src.model import Product
from collection import ProductCatalog


def build_catalog() -> ProductCatalog:
    catalog = ProductCatalog()
    catalog.add(Product("Laptop", 1200, discount=10, stock=5))
    catalog.add(Product("Mouse", 50, discount=0, stock=20))
    catalog.add(Product("Keyboard", 90, discount=5, stock=0))
    catalog.add(Product("Monitor", 300, discount=15, stock=7, active=False))
    return catalog


def scenario_1_basic_usage() -> None:
    print("SCENARIO 1")
    catalog = build_catalog()
    print("len:", len(catalog))
    for product in catalog:
        print(product)
    found = catalog.find_by_name("Mouse")
    print("found:", found)
    print("\n")


def scenario_2_duplicate_and_removal() -> None:
    print("SCENARIO 2")
    catalog = build_catalog()
    try:
        catalog.add(Product("Mouse", 60, discount=0, stock=1))
    except Exception as exc:
        print(type(exc).__name__, exc)
    catalog.remove(catalog.find_by_name("Keyboard"))
    for product in catalog:
        print(product)
    print("\n")


def scenario_3_indexing_sorting_filtering() -> None:
    print("SCENARIO 3")
    catalog = build_catalog()
    print("\nindex 0:", catalog[0])
    print("\nindex 1:", catalog[1])
    catalog.sort_by_name()
    print("\nsorted by name:")
    for product in catalog:
        print(product)
    catalog.sort_by_price(reverse=True)
    print("\nsorted by price desc:")
    for product in catalog:
        print(product)
    active_catalog = catalog.get_active()
    available_catalog = catalog.get_available()
    expensive_catalog = catalog.get_expensive(100)
    print("\nactive:")
    for product in active_catalog:
        print(product)
    print("\navailable:")
    for product in available_catalog:
        print(product)
    print("\nexpensive:")
    for product in expensive_catalog:
        print(product)
    removed = catalog.remove_at(0)
    print("\nremoved_at_0:", removed)
    print("\nafter remove_at:")
    for product in catalog:
        print(product)
    print()


def main() -> None:
    scenario_1_basic_usage()
    scenario_2_duplicate_and_removal()
    scenario_3_indexing_sorting_filtering()


if __name__ == "__main__":
    main()
