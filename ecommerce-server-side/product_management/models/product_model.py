from datetime import datetime
from ecommerce.db_config import db


class ProductsModel(db.Model):
    __table_name__ = "products"
    __table_args__= {"schema":"products_schema"}

    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String)
    product_description = db.Column(db.String)
    category  = db.Column(db.String)
    price  = db.Column(db.Float)
    quantity_in_stock  = db.Column(db.Integer)
    sku = db.Column(db.Integer)
    supplier_id  = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())