from flask import Flask
from ecommerce.db_config import db, app  # Import database config
from ecommerce.controllers.auth_controllers import blp_auth

# Register the blueprint
app.register_blueprint(blp_auth)

# Initialize the app
@app.route('/')
def home():
    return "E-commerce Dashboard Backend Running!"

with app.app_context():
    db.create_all()  # Create tables
    print("Database connected and tables created successfully!")

if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask
# from ecommerce.db_config import db, app  # Import database config
# from ecommerce.controllers.auth_controllers import blp_auth

# # Register the blueprint
# app.register_blueprint(blp_auth)
# # Initialize the app
# @app.route('/')
# def home():
#     return "E-commerce Dashboard Backend Running!"


# with app.app_context():
#     db.create_all()
#     print("Database connected and tables created successfully!")


# if __name__ == '__main__':
#     app.run(debug=True)


# # Set up basic routes for User, Product, and Order services
# @app.route('/products')
# def get_products():
#     return get_products

# @app.route('/users')
# def get_users():
#     return "<p>hello_world</p>"

# @app.route('/orders')
# def get_orders():
#     return get_orders

# # POST /register → Register new admin user
# # POST /login → Authenticate user
# # GET /products → Fetch all products
# # POST /products → Add new product
# # GET /orders → Fetch all orders

# if __name__ == '__main__':
#     app.run(debug=True)
