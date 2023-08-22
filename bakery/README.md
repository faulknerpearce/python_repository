# Bakery Inventory 
This program models a bakery's inventory and implements functionality to:

- Lookup stock levels and pricing for baked goods
- Calculate the total value of a baked good currently in stock
- Simulate selling a quantity of a baked good
- Reduces the item's stock level
- Increases the item's price based on remaining value
- This provides basic business analytics for managing inventory.

## Code Overview
The bakery dictionary contains the inventory with keys for item names and nested price/stock dictionaries.

### total_value()

- Accepts the inventory and an item name
- Checks if the item exists in the inventory
- Calculates the total value by multiplying price * stock
- Returns the total value

### buy_item()

- Accepts the inventory, item name, and amount to purchase
- Calls total_value() to get the prior value
- Reduces the item's stock by the amount
- Calculates a new price based on prior value divided by remaining stock
- Returns a confirmation with new price
- This allows simulating buying items and maintaining consistent total value.