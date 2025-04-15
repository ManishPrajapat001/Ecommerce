from flask import jsonify, make_response
from ecommerce.db_config import db
from product_management.repositories.product_repository import ProductRepo

class ProductService:

    @classmethod
    def create_product(cls, product_name, product_description, category, price, quantity_in_stock, sku, supplier_id):
        product_details = {
            "product_name": product_name,
            "product_description": product_description,
            "category": category,
            "price": price,
            "quantity_in_stock": quantity_in_stock,
            "sku": sku,
            "supplier_id": supplier_id
        }
        db.session.add(product_details)
        db.session.commit()

        return make_response(jsonify(message="Product created successfully", status=True), 200)

    @classmethod
    def fetch_product(cls, product_id):
        details = ProductRepo.fetch_product(product_id)
        product_details = {
            "product_id": details.product_id,
            "product_name": details.product_name,
            "product_description": details.product_description,
            "category": details.category,
            "price": details.price,
            "quantity_in_stock": details.quantity_in_stock,
            "sku": details.sku,
            "supplier_id": details.supplier_id,
            "created_at" : details.created_at,
            "updated_at": details.updated_at
        }
        return make_response(jsonify(product_details=product_details, status=True), 200)

    @classmethod
    def delete_product(cls, product_id):
        ProductRepo.delete_product(product_id)
        return make_response(jsonify(message="Product deleted successfully", status=True), 200)

    @classmethod
    def update_product(cls, product_id, product_name, product_description, category, price, quantity_in_stock, sku,
                       supplier_id):
        ProductRepo.update_product(product_id, product_name, product_description, category, price, quantity_in_stock,
                                   sku, supplier_id)
        return make_response(jsonify(message="Product updated successfully", status=True), 200)


class SupplierService:

    @classmethod
    def create_supplier(cls, supplier_name, contact_email, phone_number, address):
        supplier_details = {
            "supplier_name": supplier_name,
            "contact_email": contact_email,
            "phone_number": phone_number,
            "address": address
        }
        db.session.add(supplier_details)
        db.session.commit()

        return make_response(jsonify(message="Product created successfully", status=True), 200)
