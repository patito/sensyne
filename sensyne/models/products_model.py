from db import db


class ProductsModel(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)

    def json(self):
        return {
            "id": self.id,
            "price": self.price,
            "name": self.name,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_product_id(cls, product_id):
        return cls.query.filter_by(id=product_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
