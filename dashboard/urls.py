from . import views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path(
        'dashboard',
        views.DashboardView.as_view(),
        name='dashboard'
    )
]
