from django.urls import path
from .views.main_view import index
from .views.auth_view import login_method, register_method,logout_method

urlpatterns = [
    path('',index , name="index"),
    path('login/',login_method , name="login"),
    path('register/',register_method, name="register"),
    path('logout/',logout_method, name="logout")
]
