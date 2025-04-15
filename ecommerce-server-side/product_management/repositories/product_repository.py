from ecommerce.db_config import db
from product_management.models.product_model import ProductsModel

class ProductRepo:
    def __init__(self, product_name, product_description, category, price, quantity_in_stock, sku, supplier_id):
        self.product_name = product_name
        self.product_description = product_description
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.sku = sku
        self.supplier_id = supplier_id

    @classmethod
    def fetch_product(cls, product_id):
        return ProductsModel.query.get(product_id)

    @classmethod
    def delete_product(cls, product_id):
        product = ProductsModel.query.get(product_id)
        db.session.delete(product)
        db.session.commit()

    @classmethod
    def update_product(cls, product_id, product_name, product_description, category, price, quantity_in_stock, sku,
                       supplier_id):
        query = ProductsModel.query.get(product_id)
        query.update({
            "product_name": product_name,
            "product_description": product_description,
            "category": category,
            "price": price,
            "quantity_in_stock": quantity_in_stock,
            "sku": sku,
            "supplier_id": supplier_id
        })
        db.session.commit()
