from blog import db
from werkzeug.security import check_password_hash, generate_password_hash


# class UserModel(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(20))
#     passwordcity = db.Column(db.String(20))

#     def __init__(self, name: str, city: str):
#         self.name = name
#         self.city = city


class UserRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password = db.Column(db.String(200))

    def __init__(self, name: str, user_name: str, password: str):
        self.name = name
        self.username = user_name
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password, password)
