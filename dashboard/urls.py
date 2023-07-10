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
        'leads/overview/',
        leads_views.LeadView.as_view(),
        name='leads_overview'
    ),
    path(
        'leads/category/',
        leads_views.CategoryView.as_view(),
        name='leads_category'
    ),
    path(
        'leads/category/search',
        leads_views.CategorySearchView.as_view(),
        name='leads_category_search'
    ),
    path(
        'leads/category/<int:pk>/delete/',
        leads_views.CategoryDeleteView.as_view(),
        name='leads_category_delete'
    ),
]
