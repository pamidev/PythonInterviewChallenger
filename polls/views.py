from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello adventurer. You're at the main page.")
