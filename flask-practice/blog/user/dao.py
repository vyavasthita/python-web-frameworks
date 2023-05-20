from blog import db
from blog.user.models import User
from blog import login


class UserDao:
    @login.user_loader
    def load_user(id):
        return user_dao.get_user_by_id(id)

    def get_all_users(self):
        return User.query.all()
    
    def register_user(self, name: str, username: str, password: str):
        user = User(name, username, password)
        db.session.add(user)
        db.session.commit()

    def check_user_exists(self, username: str):
        return True if User.query.filter_by(username=username).first() is not None else False
    
    def get_user(self, username: str):
        return User.query.filter_by(username=username).first()
    
    def get_user_by_id(self, id):
        return User.query.get(int(id))

user_dao = UserDao()