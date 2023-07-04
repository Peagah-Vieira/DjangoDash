from django.shortcuts import render
from .forms import RegisterForm


def login_view(request):
    return render(request, 'login_view.html')


def register_view(request):
    form = RegisterForm()
    return render(request, 'register_view.html', context={
        'form': form
    })
