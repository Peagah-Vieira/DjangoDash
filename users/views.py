from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib import messages


def register_view(request):
    form = RegisterForm()
    return render(request, 'register_view.html', context={
        'form': form,
        'form_action': reverse('users:register_create')
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
    form = LoginForm()
    return render(request, 'login_view.html', context={
        'form': form,
        'form_action': reverse('users:login_create')
    })


def login_create(request):
    if not request.POST:
        raise Http404()

    form = LoginForm(request.POST)

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password'),
        )

        if authenticated_user:
            messages.success(request, 'You are logged in.')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        messages.error(request, 'Invalid credentials.')

    return redirect(reverse('users:login'))
