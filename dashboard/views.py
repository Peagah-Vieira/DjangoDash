from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


class DashboardView(LoginRequiredMixin, generic.View):
    login_url = "users:login"
    template_name = 'dashboard/pages/dashboard_home.html'

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


class DashboardProfileView(LoginRequiredMixin, generic.View):
    login_url = "users:login"
    template_name = 'dashboard/pages/my_profile.html'

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
