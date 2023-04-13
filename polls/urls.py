from django.urls import path
from .views import add_question, quiz
from django.views.generic import TemplateView


urlpatterns = [
    path('base', TemplateView.as_view(template_name='base.html'), name='base'),
    path('test', TemplateView.as_view(template_name='test.html'), name='test'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('quiz', quiz, name='quiz'),
    path('add_question', add_question, name='add_question')
]
