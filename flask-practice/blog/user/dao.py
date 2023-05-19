from blog import db
from blog.user.models import UserModel


class UserDao:
    def create_user(self, name:str, city: str) -> None:
        user = UserModel(name, city)
        db.session.add(user)
        db.session.commit()

user_dao = UserDao()