from flask import  Blueprint, request
from shopping_cart.services.shopping_cart_service import ShoppingCartService

blp_cart = Blueprint('blp_cart',__name__,url_prefix='/api/shopping-cart')

class ShoppingCartController:

    @blp_cart.post("/create-cart")
    def create_cart():
        req = request.json
        customer_id = req["customer_id"]
        status = req["status"]
        product_id = req["product_id"]
        quantity = req["quantity"]
        price_at_time = req["price_at_time"]
        discount = req["discount"]
        coupon_code = req["coupon_code"]
        shipping_address_id = req["shipping_address_id"]
        payment_method = req["payment_method"]
        payment_status = req["payment_status"]
        return ShoppingCartService.create_cart(customer_id, status, product_id, quantity, price_at_time, discount,
                                                    coupon_code, shipping_address_id, payment_status, payment_method)

    @blp_cart.get("/fetch-cart/<int:cart_id>")
    def fetch_cart(cart_id):
        return ShoppingCartService.fetch_cart(cart_id)

    @blp_cart.delete("/delete-cart/<int:cart_id>")
    def delete_cart(cart_id):
        return ShoppingCartService.delete_cart(cart_id)

    @blp_cart.put("/update-cart/<int:cart_id>")
    def update_cart(cart_id):
        req = request.json
        customer_id = req["customer_id"]
        status = req["status"]
        product_id = req["product_id"]
        quantity = req["quantity"]
        price_at_time = req["price_at_time"]
        discount = req["discount"]
        coupon_code = req["coupon_code"]
        shipping_address_id = req["shipping_address_id"]
        payment_method = req["payment_method"]
        payment_status = req["payment_status"]
        return ShoppingCartService.update_cart(cart_id, customer_id, status, product_id, quantity, price_at_time, discount,
                                               coupon_code, shipping_address_id, payment_status, payment_method)
