import os
from typing import Any

from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_restful import Api

import routes
from db import db


def create_app(config: Any = None) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    from sensyne.models.products_model import ProductsModel  # noqa

    return app


app = create_app()
api = Api(app)
routes.add(api)


@app.errorhandler(404)
def resource_not_found(e):  # type: ignore
    return jsonify(error=str(e)), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
