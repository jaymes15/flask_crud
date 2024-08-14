from db import db

class ItemsTags(db.Model):
    __tablename__ = "items_tags"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))

    def __repr__(self):
        return f"<ItemsTags(id={self.id}, item_id={self.item_id}, tag_id={self.tag_id})>"

    def __str__(self):
        return f"Item ID: {self.item_id}, Tag ID: {self.tag_id}"
