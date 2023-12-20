from fastapi import APIRouter


user_router = APIRouter(prefix='/user')

@user_router.get('/<username>')
def user_info(username):
    return 'Namaste,' + username