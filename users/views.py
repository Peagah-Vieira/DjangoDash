from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.http import Http404
from django.urls import reverse


def register_view(request):
    form = RegisterForm()
    return render(request, 'register_view.html', context={
        'form': form
    })


def register_create(request):
    if not request.POST:
        return redirect('users:register')

    details = RegisterForm(request.POST)

    if details.is_valid():
        user = details.save(commit=False)
        user.set_password(user.password)
        user.save()
        return redirect(reverse('users:login'))

    return render(request, 'register_view.html', context={
        'form': details
    })


def login_view(request):
    return render(request, 'login_view.html')


def login_create(request):
    if not request.POST:
        raise Http404()

    return redirect(reverse('users:login'))
