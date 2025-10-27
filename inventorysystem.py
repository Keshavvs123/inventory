"""
Inventory System module to manage stock, add, remove, save, and load items.
"""
import json
import logging
from datetime import datetime

stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """
    Add a quantity of an item to the stock.

    Args:
        item (str): The name of the item.
        qty (int): Quantity to add.
        logs (list): List to record log entries.

    Returns:
        None
    """
    if logs is None:
        logs = []
    if not item or not isinstance(item, str) or not isinstance(qty, int):
        return
    new_qty = stock_data.get(item, 0) + qty
    if new_qty < 0:
        return
    stock_data[item] = new_qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """
    Remove a quantity of an item from the stock.

    Args:
        item (str): The name of the item.
        qty (int): Quantity to remove.

    Returns:
        None
    """
    try:
        if not isinstance(qty, int) or qty < 0:
            return
        if stock_data.get(item, 0) < qty:
            return
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass
    except TypeError:
        pass

def get_qty(item):
    """
    Get quantity of an item in stock.

    Args:
        item (str): The name of the item.

    Returns:
        int: Quantity available.
    """
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """
    Load stock data from a JSON file.

    Args:
        file (str): Filename to load data from.

    Returns:
        None
    """
    global stock_data
    with open(file, "r", encoding="utf-8") as f:
        stock_data = json.load(f)

def save_data(file="inventory.json"):
    """
    Save stock data to a JSON file.

    Args:
        file (str): Filename to save data to.

    Returns:
        None
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f)

def print_data():
    """
    Print the current inventory data.
    """
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")

def check_low_items(threshold=5):
    """
    Check and return the list of items with quantity below threshold.

    Args:
        threshold (int): Quantity below which items are considered low.

    Returns:
        list: List of low stock items.
    """
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    load_data()
    print_data()
    print("eval used")  # dangerous

main()