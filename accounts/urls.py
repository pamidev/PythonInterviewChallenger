from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginPage, name='user_login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.registerPage, name='register'),
]
