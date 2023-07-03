from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'users/pages/login_view.html')
