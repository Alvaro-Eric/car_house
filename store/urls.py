from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('checkout/', views.checkout, name="checkout"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),


]
