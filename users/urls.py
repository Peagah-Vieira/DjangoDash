from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path(
        'login/',
        views.login_view,
        name='login'
    ),
    path(
        'login/create',
        views.login_create,
        name='login_create'
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
