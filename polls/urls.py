from django.urls import path
from .views import add_question, quiz

urlpatterns = [
    path('', quiz, name='home'),
    path('add_question/', add_question, name='add_question')
]
