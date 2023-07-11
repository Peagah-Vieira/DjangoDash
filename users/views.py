from django.shortcuts import render, redirect
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetConfirmView
)
from .forms import (
    RegisterForm,
    LoginForm,
    PasswordResetCustomForm,
    SetPasswordCustomForm
)


class RegisterView(generic.CreateView):
    form = RegisterForm
    template_name = 'users/register.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        url = reverse_lazy('dashboard:home')

        if request.user.is_authenticated:
            return redirect(url)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        url = reverse_lazy('users:login')

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            messages.success(request, 'Successfully Registered')
            return redirect(url)

        return render(request, self.template_name, context=context)


class LoginView(generic.View):
    form = LoginForm
    template_name = 'users/login.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        url = reverse_lazy('dashboard:home')

        if request.user.is_authenticated:
            return redirect(url)

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = self.form()
        context = {'form': form}
        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form(request.POST)
        url = reverse_lazy('users:login')

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            authenticated_user = authenticate(
                username=username,
                password=password
            )

            if authenticated_user:
                dashboard_url = reverse_lazy('dashboard:home')
                login(request, authenticated_user)
                return redirect(dashboard_url)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid credentials.')

        return redirect(url)


class LogoutView(LoginRequiredMixin, generic.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        raise Http404()

    def post(self, request):
        url = reverse_lazy('users:login')
        messages.success(request, 'Logged out successfully')
        logout(request)
        return redirect(url)


class PasswordResetCustomView(SuccessMessageMixin, PasswordResetView):
    form_class = PasswordResetCustomForm
    email_template_name = 'users/mail/password_reset_email.html'
    subject_template_name = 'users/mail/password_reset_subject.txt'
    template_name = 'users/password_reset.html'
    success_message = "We've emailed you instructions for setting your password"  # noqa
    success_url = reverse_lazy('users:login')


class PasswordResetConfirmCustomView(SuccessMessageMixin, PasswordResetConfirmView):  # noqa
    form_class = SetPasswordCustomForm
    template_name = "users/password_reset_confirm.html"
    success_message = "Your password has been set. You may go ahead and Login"  # noqa
    success_url = reverse_lazy('users:login')


class UserProfileView(LoginRequiredMixin, generic.View):
    login_url = "users:login"
    template_name = 'dashboard/pages/dashboard_profile.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        ...
