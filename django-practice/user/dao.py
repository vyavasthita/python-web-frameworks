from .models import Registration


class UserDao:
    def get_all_users(self):
        return list(Registration.objects.all())

user_dao = UserDao()