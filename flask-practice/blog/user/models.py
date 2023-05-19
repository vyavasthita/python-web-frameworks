from blog import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String)

    def __init__(self, name: str, city: str):
        self.name = name
        self.city = city