from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    path('login/', views.login_view, name='login')
]
