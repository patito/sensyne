from flask import request
from flask_restful import Resource

from sensyne.models.products_model import ProductsModel


class ProductsView(Resource):
    def get(self):
        products = ProductsModel.find_all()
        return [product.json() for product in products]


class ProductView(Resource):
    def post(self):
        data = request.get_json()

        product = ProductsModel(**data)
        product.save_to_db()

        return product.json()


class ProductsItemView(Resource):
    def get(self, product_id):
        product = ProductsModel.find_by_product_id(product_id)
        if not product:
            return {"message": f"Product {product_id} not found"}, 404

        return product.json()

    def put(self, product_id):
        product = ProductsModel.find_by_product_id(product_id)
        if not product:
            return {"message": f"Product {product_id} not found"}, 404

        data = request.get_json()
        product.name = data.get("name", product.name)
        product.price = data.get("price", product.price)

        product.save_to_db()

        return product.json(), 200

    def delete(self, product_id):
        product = ProductsModel.find_by_product_id(product_id)
        if not product:
            return {"message": f"Product {product_id} not found"}, 404

        product.delete_from_db()

        return {"message": f"Product {product_id} removed"}, 200
