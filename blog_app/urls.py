from django.urls import path
from .views.main_view import index,create_blog,single_method,delete_blog
from .views.auth_view import login_method, register_method,logout_method

urlpatterns = [
    path('',index , name="index"),
    path('login/',login_method , name="login"),
    path('register/',register_method, name="register"),
    path('logout/',logout_method, name="logout"),
    path('create/',create_blog, name="create"),
    path('single/<int:id>/',single_method, name="single"),
    path('delete/<int:id>/',delete_blog, name="delete")
]
