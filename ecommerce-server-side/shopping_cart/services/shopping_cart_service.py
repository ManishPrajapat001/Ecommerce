from flask import jsonify, make_response
from ecommerce.db_config import db
from shopping_cart.repositories.shopping_cart_repository import ShoppingCartRepo

class ShoppingCartService:

    @classmethod
    def create_cart(cls, customer_id, status, product_id, quantity, price_at_time, discount, coupon_code,
                    shipping_address_id, payment_status, payment_method):
        total_price = quantity*price_at_time
        cart_details = {
            "customer_id": customer_id,
            "status": status,
            "product_id": product_id,
            "quantity": quantity,
            "price_at_time": price_at_time,
            "discount": discount,
            "coupon_code": coupon_code,
            "shipping_address_id": shipping_address_id,
            "payment_status": payment_status,
            "payment_method": payment_method,
            "total_price": total_price
        }
        db.session.add(cart_details)
        db.session.commit()

        return make_response(jsonify(message="Cart created successfully", status=True), 200)

    @classmethod
    def fetch_cart(cls, cart_id):
        details = ShoppingCartRepo.fetch_cart(cart_id)
        cart_details = {
            "cart_id": cart_id,
            "customer_id": details.customer_id,
            "status": details.status,
            "product_id": details.product_id,
            "quantity": details.quantity,
            "price_at_time": details.price_at_time,
            "discount": details.discount,
            "coupon_code": details.coupon_code,
            "shipping_address_id": details.shipping_address_id,
            "payment_status": details.payment_status,
            "payment_method": details.payment_method,
            "total_price": details.total_price,
            "created_at" : details.created_at,
            "updated_at": details.updated_at
        }
        return make_response(jsonify(cart_details=cart_details, status=True), 200)

    @classmethod
    def delete_cart(cls, cart_id):
        ShoppingCartRepo.delete_cart(cart_id)
        return make_response(jsonify(message="Cart deleted successfully", status=True), 200)

    @classmethod
    def update_cart(cls,cart_id, customer_id, status, product_id, quantity, price_at_time, discount, coupon_code,
                    shipping_address_id, payment_status, payment_method):
        total_price = quantity*price_at_time
        ShoppingCartRepo.update_cart(cart_id, customer_id, status, product_id, quantity, price_at_time, discount, coupon_code,
                    shipping_address_id, payment_status, payment_method, total_price)
        return make_response(jsonify(message="Cart updated successfully", status=True), 200)
