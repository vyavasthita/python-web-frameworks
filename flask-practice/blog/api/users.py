from blog.api import api_blueprint
from blog.user.dao import user_dao


@api_blueprint.route('/users', methods=['GET'])
def get_users():
    users = user_dao.get_all_users()

    all_users = list()

    for user in users:
        info = dict()
        info['name'] = user.name
        info['username'] = user.username

        all_users.append(info)

    return all_users

@api_blueprint.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    pass

