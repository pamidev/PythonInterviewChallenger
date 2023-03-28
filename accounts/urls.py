from django.urls import path
from .views import CustomLoginView
from polls.views import index


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('accounts/profile/', index, name='profil'),
]
