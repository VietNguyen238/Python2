from django.urls import path
from . import views

urlpatterns = [
	path('home/', views.index),
    path('contact/', views.contact),
    path("register/", views.register, name="register"),
    path("", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]
