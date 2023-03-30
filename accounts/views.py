from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin

from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')


class CustomUserRegistrationView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration.html'

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(CustomUserRegistrationView, cls).as_view(**initkwargs)
        view.form_class = cls.form_class
        view.success_url = cls.success_url
        view.template_name = cls.template_name
        return view


def profile(request):
    return HttpResponse("Hello. This is Your profile.")
