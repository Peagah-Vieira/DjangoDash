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
        raise Http404()

    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        return redirect(reverse('users:login'))

    return redirect('users:register')


def login_view(request):
    return render(request, 'login_view.html')


def login_create(request):
    if not request.POST:
        raise Http404()

    return redirect(reverse('users:login'))
