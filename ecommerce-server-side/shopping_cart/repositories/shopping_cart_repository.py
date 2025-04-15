from ecommerce.db_config import db
from shopping_cart.models.shopping_cart_model import ShoppingCart

class ShoppingCartRepo:
    def __init__(self):
        pass

    @classmethod
    def fetch_cart(cls, cart_id):
        return ShoppingCart.query.get(cart_id)

    @classmethod
    def delete_cart(cls, cart_id):
        cart = ShoppingCart.query.get(cart_id)
        db.session.delete(cart)
        db.session.commit()

    @classmethod
    def update_cart(cls, cart_id, customer_id, status, product_id, quantity, price_at_time, discount, coupon_code,
                    shipping_address_id, payment_status, payment_method, total_price):
        query = ShoppingCart.query.get(cart_id)
        query.update({
            "cart_id": cart_id,
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
        })
        db.session.commit()