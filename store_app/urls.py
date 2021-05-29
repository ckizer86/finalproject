from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.login_page),
    path('loginuser', views.login),
    path('register', views.register_page),
    path('registeruser', views.register),
    path('cat/<int:id>', views.category),
    path('product/<int:id>', views.product),
    path('add_cart', views.addcart),
    path('cart', views.cart),
    path('config/', views.stripe_config),
    path('create-checkout-session/', views.create_checkout_session),
    path('success/', views.SuccessView),
    path('cancelled/', views.CancelledView),
    path('webhook/', views.stripe_webhook),
]