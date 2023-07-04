from django.shortcuts import render


def login_view(request):
    return render(request, 'login_view.html')


def register_view(request):
    return render(render, 'register_view.html')
