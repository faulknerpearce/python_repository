# Bakery Inventory Management

## Overview

The Bakery Inventory Management, This program facilitates key functionalities including stock lookup, total value calculation, and simulated sales for accurate business analytics.

## Features

- Quickly retrieve stock levels and pricing for various baked goods.
- Calculate the total value of specific items currently in stock.
- Implement a simulation for selling a specified quantity of a baked good.
- Automatically adjust prices based on remaining value and stock levels.

## Code Overview

The central data structure, `bakery_inventory`, contains the inventory with keys for item names and nested dictionaries for price and stock levels.

### Functions

`total_value(inventory, item)`

- Accepts the bakery inventory and the name of the item.
- Checks if the item is present in the inventory.
- Calculates the total value as the product of price and stock.
- Returns the total value.

`buy_item(inventory, item, amount)`

- Accepts the bakery inventory, item name, and quantity to purchase.
- Utilizes `total_value()` to obtain the prior value.
- Decreases the item's stock by the specified amount.
- Computes a new price using the prior value divided by the remaining stock.
- Returns a confirmation message with the updated price.

## Usage

1. Define your bakery inventory, specifying items along with their respective prices and initial stock levels.
2. Utilize the `total_value` function to ascertain the total value of remaining stock for a specific item.
3. Employ the `buy_item` function to adjust item prices based on changes in stock.

