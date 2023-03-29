from django.urls import path
from .views import CustomLoginView
from accounts.views import profile


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/profile/', profile, name='profil'),
]
