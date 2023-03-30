from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logour/', views.logoutUser, name='logout'),
    path('accounts/profile/', views.profile, name='profil'),
    path('register/', views.registerPage, name='register'),
]
