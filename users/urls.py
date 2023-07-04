from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/create', views.login_create, name='login_create'),
    path('register/', views.register_view, name='register'),
    path('register/create/', views.register_create, name='register_create')
]
