from sensyne.views.products_views import ProductView, ProductsView, ProductsItemView


def add(api):
    # Add all views register here
    api.add_resource(ProductView, "/v1/product")
    api.add_resource(ProductsView, "/v1/products")
    api.add_resource(ProductsItemView, "/v1/product/<product_id>")
