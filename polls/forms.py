from django.forms import ModelForm
from .models import *


class AddQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
