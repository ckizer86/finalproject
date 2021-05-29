from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login_page),
    path('loginuser', views.login),
    path('register', views.register_page),
    path('registeruser', views.register),
    path('cat/<int:id>', views.category),
]