from django.contrib import admin
from .models import Category, Agent, Lead


class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]
    list_display = [
        'id',
        'name',
        'description',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'name',
        'description',
    ]
    list_filter = [
        'created_at',
        'updated_at',
    ]
    list_per_page = 10
    ordering = ['-id']


class AgentAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        'created_at',
        'updated_at',
    ]
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'first_name',
        'last_name',
    ]
    list_filter = [
        'created_at',
        'updated_at',
    ]
    list_per_page = 10
    ordering = ['-id']


class LeadAdmin(admin.ModelAdmin):
    search_fields = [
        'id',
        'first_name',
        'last_name',
        'email',
        'age',
        'category__name',
        'agent__first_name',
        'created_at',
        'updated_at',
    ]
    list_display = [
        'id',
        'first_name',
        'last_name',
        'email',
        'age',
        'category',
        'agent',
        'created_at',
        'updated_at',
    ]
    list_display_links = [
        'first_name',
        'last_name',
    ]
    list_filter = [
        'created_at',
        'updated_at',
    ]
    list_per_page = 10
    ordering = ['-id']


admin.site.register(Category, CategoryAdmin)

admin.site.register(Agent, AgentAdmin)

admin.site.register(Lead, LeadAdmin)
