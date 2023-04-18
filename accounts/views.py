from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateUserForm


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username is already taken.')
                else:
                    form.save()
                    user = form.cleaned_data.get('username')
                    messages.success(request, 'Account was created for ' + user)
                    return redirect('user_login')

        context = {'form': form}
        return render(request, 'accounts/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or password is incorrect')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return render(request, 'accounts/logout.html')


def profile(request):
    return render(request, 'accounts/profile.html')
