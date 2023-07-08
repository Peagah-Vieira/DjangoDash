from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.http import Http404
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, View
from django.utils.decorators import method_decorator


class RegisterView(CreateView):
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


class LoginView(View):
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


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class LogoutView(View):
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
