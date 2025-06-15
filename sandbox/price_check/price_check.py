def priceCheck(products, productPrices, productSold, soldPrice):

    items = dict(zip(products, productPrices))

    errors = 0

    for product, actual_price in zip(productSold, soldPrice):

        try: 
            expected_price = items[product]

            if expected_price != actual_price:
                errors += 1

        except KeyError:
            errors += 1

    return errors

if __name__ == '__main__':

    products = ['rice', 'sugar', 'wheat', 'cheese']

    productPrices = [16.89, 56.92, 20.89, 345.99]
    
    productSold = ['rice', 'cheese']
    
    soldPrice = [18.99, 400.89]

    result = priceCheck(products, productPrices, productSold, soldPrice)

    print(result)