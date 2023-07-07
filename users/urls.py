from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ),
    path(
        'logout/',
        views.logout_view,
        name="logout"
    ),
]
