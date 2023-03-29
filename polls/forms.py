from django.forms import ModelForm
from .models import *


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'answer_1', 'answer_2', 'answer_3', 'answer_4', 'correct_answer']
