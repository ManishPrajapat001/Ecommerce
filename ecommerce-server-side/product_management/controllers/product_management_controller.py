from flask import  Blueprint, request
from product_management.services.product_management_service import ProductService

blp_products = Blueprint('blp_products',__name__,url_prefix='/api/products')

class ShoppingCartController:

    @blp_products.post("/create-product")
    def create_cart():
        req = request.json
        product_name = req["product_name"]
        product_description = req["product_description"]
        category = req["category"]
        price = req["price"]
        quantity_in_stock = req["quantity_in_stock"]
        sku = req["sku"]
        supplier_id = req["supplier_id"]
        return ProductService.create_product(product_name, product_description, category, price, quantity_in_stock, sku,
                                             supplier_id)

    @blp_products.get("/fetch-product/<int:product_id>")
    def fetch_product(product_id):
        return ProductService.fetch_product(product_id)

    @blp_products.delete("/fetch-product/<int:product_id>")
    def delete_product(product_id):
        return ProductService.delete_product(product_id)

    @blp_products.put("/update-product/<int:product_id>")
    def update_product(product_id):
        req = request.json
        product_name = req["product_name"]
        product_description = req["product_description"]
        category = req["category"]
        price = req["price"]
        quantity_in_stock = req["quantity_in_stock"]
        sku = req["sku"]
        supplier_id = req["supplier_id"]
        return ProductService.update_product(product_id, product_name, product_description, category, price,
                                             quantity_in_stock, sku, supplier_id)
