from django.urls import path, include
from .views import *
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<slug>', CategoryView.as_view(), name='category'),
    path('brand/<slug>', BrandView.as_view(), name='brand'),
    path('product/<slug>', ProductDetail.as_view(), name='product'),
    path('search', SearchView.as_view(), name='search'),
    path('signup', signup, name='signup'),
    path('cart', CartView.as_view(), name='cart'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_to_cart/<slug>', add_to_cart, name='add_to_cart'),
    path('reduce_cart/<slug>', reduce_cart, name='reduce_cart'),
    path('delete_cart/<slug>', delete_cart, name='delete_cart'),
    path('product_review/<slug>', product_review, name='product_review'),

]
