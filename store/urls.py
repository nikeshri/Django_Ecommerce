from django.urls import path,include
from . import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("main", views.main, name="main"),
    path("cart", views.cart,name="cart"),
    path("login", views.login, name="login"),
    path("blogs", views.blogs,name="blogs"),
    path("contact", views.contact, name="contact")
]