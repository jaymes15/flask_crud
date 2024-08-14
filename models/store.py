from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    tags = db.relationship("TagModel", back_populates="store", lazy="dynamic")
    items = db.relationship("ItemModel", back_populates="store", lazy="dynamic")

    def __repr__(self):
        return f"<StoreModel(id={self.id}, name='{self.name}')>"

    def __str__(self):
        return f"Store(name='{self.name}', id={self.id})"
