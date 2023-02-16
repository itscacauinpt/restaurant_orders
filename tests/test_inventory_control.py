# import pytest
from src.inventory_control import InventoryControl


def test_update_current_inventory():
    inventory = InventoryControl()

    inventory.add_new_order("customer", "hamburguer", "terça-feira")
    inventory.add_new_order("customer", "hamburguer", "terça-feira")

    total_ingredients = {
        "pao": 2,
        "carne": 2,
        "queijo": 2,
        "molho": 0,
        "presunto": 0,
        "massa": 0,
        "frango": 0,
    }

    assert inventory.get_quantities_to_buy() == total_ingredients
