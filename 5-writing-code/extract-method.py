def process_order(order):
    # Validate order
    if not order['item_id'] or not order['quantity']:
        return "Invalid order: Missing item ID or quantity."
    
    # Calculate total price
    item_price = get_item_price(order['item_id'])
    if item_price is None:
        return "Invalid order: Item not found."
    
    total_price = item_price * order['quantity']
    
    # Apply discount if applicable
    if order['quantity'] > 10:
        discount = total_price * 0.1  # 10% discount for large orders
        total_price -= discount
    
    # Process payment
    payment_status = process_payment(order['payment_info'], total_price)
    if not payment_status:
        return "Payment failed."
    
    # Generate order confirmation
    confirmation = generate_confirmation(order, total_price)
    
    return confirmation
