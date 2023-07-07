from . import views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path(
        '',
        views.LandingView.as_view(),
        name='landing'
    ),
    path(
        'dashboard/',
        views.DashboardView.as_view(),
        name='home'
    )
]
