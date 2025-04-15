from datetime import datetime
from ecommerce.db_config import db


class ShoppingCart(db.Model):
    __table_name__ = "shopping_cart"
    __table_args__= {"schema":"shopping_cart_schema"}

    cart_id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer)
    # status - active, pending, abandoned
    status = db.Column(db.String)
    product_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    price_at_time = db.Column(db.Float)
    total_price = db.Column(db.Float)
    discount = db.Column(db.Float)
    coupon_code = db.Column(db.String)
    shipping_address_id = db.Column(db.Integer)
    #payment_method - cod, upi, card
    payment_method = db.Column(db.String)
    # payment_status - pending, paid, failed
    payment_status = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())