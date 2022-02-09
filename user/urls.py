
from django.urls import path
from user.views import user_login, user_logout, user_register


urlpatterns = [
    path('user-logout', user_logout, name='user_logout'),
    path('user-register', user_register, name='user_register'),
    path('login-form/', user_login, name='user_login'),
    path('register-form/', user_login, name='user_register'),
]