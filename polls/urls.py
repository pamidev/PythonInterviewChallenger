from django.urls import path
from .views import add_question, quiz


urlpatterns = [
    path('quiz/', quiz, name='quiz'),
    path('add_question/', add_question, name='add_question'),
]
