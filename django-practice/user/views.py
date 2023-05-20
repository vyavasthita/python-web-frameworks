from django.shortcuts import render
from .dao import user_dao


def home(request):
    return render(request, 'home.html', {'users': user_dao.get_all_users()})
