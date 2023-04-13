from django.urls import path
from django.views.generic import TemplateView

from .views import add_question, quiz


urlpatterns = [
    path('quiz/', quiz, name='quiz'),
    path('add_question/', add_question, name='add_question'),
    path('thanks/', TemplateView.as_view(template_name='polls/thanks.html'), name='thanks'),
]
