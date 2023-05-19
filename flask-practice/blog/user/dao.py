from blog import db
from blog.user.models import UserRegistration


class UserDao:
    def get_all_users(self):
        return UserRegistration.query.all()
    
    def register_user(self, name: str, username: str, password: str):
        user = UserRegistration(name, username, password)
        db.session.add(user)
        db.session.commit()

    def check_user_exists(self, username: str):
        user = UserRegistration.query.filter_by(username=username).first()

        return True if user is not None else False
    
    def get_user(self, username: str):
        return UserRegistration.query.filter_by(username=username).first()

user_dao = UserDao()