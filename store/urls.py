from django.urls import path 
from . import views 

from store.controller import AuthenticationController

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', AuthenticationController.loginFunction, name="login"),
    path('register/', AuthenticationController.register, name="register"),
    path('logout/', AuthenticationController.logoutFunction, name="logout"),
    path('password/', views.password, name="password"),


    path('collections', views.collections, name="collections"),
    path('collections/<str:slug>', views.collectionsView, name="collectionsView"),
    path('products/<str:slug>', views.productsView, name="productsView"),
]