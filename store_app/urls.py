from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



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
    path('favorites', views.likeditems),
    path('dashboard', views.dashboard),
    path('dashboard/account', views.accountinfo),
    path('accountupdate', views.accountupdate),
    path('dashboard/recent_orders', views.recentorders),
    path('dashboard/order/<int:id>', views.vieworder),
    path('admin', views.admindash),
    path('admin/neworders', views.adminneworders),
    path('admin/pastorders', views.adminpastorders),
    path('admin/order/<int:id>', views.adminvieworder),
    path('updatetracking', views.updatetracking),
    path('admin/products', views.products),
    path('admin/add_product', views.addprod),
    path('addingprod', views.addingprod),
    path('admin/store', views.storeinfo),
    path('editstore', views.editstore),
    path('logout', views.logout),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)