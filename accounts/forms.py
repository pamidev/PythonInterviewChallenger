from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']

    # def clean_username(self):
    #     username = self.cleaned_data['username']
    #     if User.objects.filter(username=username).exists():
    #         raise forms.ValidationError("This username is already taken.")
    #     return username
