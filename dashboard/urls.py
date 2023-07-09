from . import views
from leads import views as leads_views
from django.urls import path

app_name = "dashboard"

urlpatterns = [
    path(
        '',
        views.DashboardView.as_view(),
        name='home'
    ),
    path(
        'leads/category/',
        leads_views.CategoryView.as_view(),
        name='leads_category'
    )
]
