bakery = {
    "Pies": {"Price": 3.00, "Stock": 75},
    "Muffins": {"Price": 4.50, "Stock": 50},
    "Cakes": {"Price": 10.00, "Stock": 100}
}
# This function returns a total value from the remaining stock. 
def total_value(inventory, item):
    if item in inventory:
        total_stock_value = inventory[item]["Price"] * inventory[item]["Stock"]
        return total_stock_value
    else: 
        return f"{item} is not listed in our bakery."
    
# This function will reduce the stock inventory and increase the unit price of the item. 
def buy_item(inventory, item, amount):
    if item in inventory:
        total_prior_value = total_value(inventory, item)
        inventory[item]["Stock"] -= amount
        updated_price = total_prior_value / inventory[item]["Stock"]

        return f"The price of {item} has increased to ${updated_price}."

print(buy_item(bakery, "Pies", 25))




    

    
