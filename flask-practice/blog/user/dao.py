from blog import db
from blog.user.models import UserModel, UserRegistration


class UserDao:
    def create_user(self, name:str, city: str) -> None:
        user = UserModel(name, city)
        db.session.add(user)
        db.session.commit()

    def get_all_users(self):
        return UserModel.query.all()
    
    def register_user(self, username: str, password: str):
        user = UserRegistration(username, password)
        db.session.add(user)
        db.session.commit()

user_dao = UserDao()