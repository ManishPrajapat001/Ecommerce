from datetime import datetime
from ecommerce.db_config import db


class SuppliersModel(db.Model):
    __table_name__ = "suppliers"
    __table_args__= {"schema":"suppliers_schema"}

    supplier_id  = db.Column(db.Integer, primary_key=True)
    supplier_name = db.Column(db.String)
    contact_email = db.Column(db.String)
    phone_number  = db.Column(db.Integer)
    address = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())