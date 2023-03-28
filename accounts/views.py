from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('home')


def profile(request):
    return HttpResponse("Hello. This is Your profile.")
