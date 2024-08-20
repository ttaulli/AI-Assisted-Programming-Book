from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for simplicity
users = {}
products = {}
orders = {}

# User Endpoints
@app.route('/users', methods=['POST'])
def create_user():
    user_id = request.json['id']
    users[user_id] = {
        "name": request.json['name'],
        "email": request.json['email'],
        "address": request.json['address']
    }
    return jsonify({"message": "User created", "user": users[user_id]}), 201

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    if user_id in users:
        return jsonify(users[user_id])
    else:
        return jsonify({"message": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"})
    else:
        return jsonify({"message": "User not found"}), 404

# Product Endpoints
@app.route('/products', methods=['POST'])
def create_product():
    product_id = request.json['id']
    products[product_id] = {
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price'],
        "stock": request.json['stock']
    }
    return jsonify({"message": "Product created", "product": products[product_id]}), 201

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    if product_id in products:
        return jsonify(products[product_id])
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products/<product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        products[product_id].update(request.json)
        return jsonify({"message": "Product updated", "product": products[product_id]})
    else:
        return jsonify({"message": "Product not found"}), 404

@app.route('/products/<product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({"message": "Product deleted"})
    else:
        return jsonify({"message": "Product not found"}), 404

# Order Endpoints
@app.route('/orders', methods=['POST'])
def create_order():
    order_id = request.json['id']
    user_id = request.json['user_id']
    if user_id not in users:
        return jsonify({"message": "User not found"}), 404

    products_ordered = request.json['products']
    for product_id in products_ordered:
        if product_id not in products or products[product_id]['stock'] < products_ordered[product_id]:
            return jsonify({"message": f"Product {product_id} is not available"}), 400
    
    orders[order_id] = {
        "user_id": user_id,
        "products": products_ordered,
        "total_price": sum(products[pid]['price'] * qty for pid, qty in products_ordered.items()),
        "status": "Pending"
    }
    
    for product_id, qty in products_ordered.items():
        products[product_id]['stock'] -= qty
    
    return jsonify({"message": "Order created", "order": orders[order_id]}), 201

@app.route('/orders/<order_id>', methods=['GET'])
def get_order(order_id):
    if order_id in orders:
        return jsonify(orders[order_id])
    else:
        return jsonify({"message": "Order not found"}), 404

@app.route('/orders/<order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    if order_id in orders:
        orders[order_id]['status'] = request.json['status']
        return jsonify({"message": "Order status updated", "order": orders[order_id]})
    else:
        return jsonify({"message": "Order not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
