from django.urls import path
from .views import add_question, quiz, index

urlpatterns = [
    path('', index, name='index'),
    path('quiz', quiz, name='quiz'),
    path('add_question/', add_question, name='add_question')
]
