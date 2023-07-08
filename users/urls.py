from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        'register/',
        views.RegisterView.as_view(),
        name='register'
    ),
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name="logout"
    ),
    path(
        'recover-password/',
        views.RecoverView.as_view(),
        name="recover-password"
    ),
]
