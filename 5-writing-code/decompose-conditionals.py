def get_discount(customer, purchase_amount):
    if customer.is_premium and purchase_amount > 100 or (customer.is_loyal and purchase_amount > 200) or (not customer.is_new and purchase_amount > 150):
        return purchase_amount * 0.1  # 10% discount
    else:
        return 0
