from db import db

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"<UserModel(id={self.id}, username='{self.username}')>"

    def __str__(self):
        return f"User(username='{self.username}', id={self.id})"
