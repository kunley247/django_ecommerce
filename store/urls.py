from django.urls import path 
from . import views 

from store.controller import AuthenticationController

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', AuthenticationController.loginFunction, name="login"),
    path('register/', AuthenticationController.register, name="register"),
    path('logout/', AuthenticationController.logoutFunction, name="logout"),
    path('password/', views.password, name="password"),


    path('category/<str:slug>', views.categoryView, name="categoryView"),
    path('products/<str:slug>', views.productsView, name="productsView"),
    path('services/<str:slug>', views.servicesView, name="servicesView"),
    path('dashboard/', views.dashboardView, name="dashboardView"),
]
