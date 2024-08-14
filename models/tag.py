from db import db

class TagModel(db.Model):
    __tablename__ = "tags"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    store_id = db.Column(db.Integer(), db.ForeignKey("stores.id"), nullable=False)

    store = db.relationship("StoreModel", back_populates="tags")
    items = db.relationship("ItemModel", back_populates="tags", secondary="items_tags")

    def __repr__(self):
        return f"<TagModel(id={self.id}, name='{self.name}', store_id={self.store_id})>"

    def __str__(self):
        return f"Tag(name='{self.name}', id={self.id}, store_id={self.store_id})"
