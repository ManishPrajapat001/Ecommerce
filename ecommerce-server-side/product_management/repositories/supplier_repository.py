from ecommerce.db_config import db
from product_management.models.supplier_model import SuppliersModel

class SupplierRepo:
    def __init__(self, product_name, product_description, category, price, quantity_in_stock, sku, supplier_id):
        self.product_name = product_name
        self.product_description = product_description
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.sku = sku
        self.supplier_id = supplier_id