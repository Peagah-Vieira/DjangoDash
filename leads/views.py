from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from leads.models import Category
from .forms import CategoryForm
from utils.pagination import make_pagination_range

import pandas


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class LeadView(generic.View):
    template_name = 'dashboard/pages/leads_overview.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        ...


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class CategoryView(generic.View):
    form = CategoryForm
    template_name = 'dashboard/pages/leads_category.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = self.form()
        categories = Category.objects.all().order_by('-id')
        current_page = int(request.GET.get('page', 1))
        paginator = Paginator(categories, per_page=10)
        page_obj = paginator.get_page(current_page)
        pagination_range = make_pagination_range(
            page_range=paginator.page_range,
            qty_pages=4,
            current_page=current_page,
        )
        context = {
            'form': form,
            'categories': page_obj,
            'pagination_range': pagination_range
        }

        return render(request, self.template_name, context=context)

    def post(self, request):
        form = self.form(request.POST)
        context = {'form': form}
        url = reverse_lazy('dashboard:leads_category')

        if form.is_valid():
            form.save()
            messages.success(request, 'Category created successfully')
            return redirect(url)

        return render(request, self.template_name, context=context)


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class CategorySearchView(CategoryView):
    form = CategoryForm
    template_name = 'dashboard/pages/leads_category.html'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        form = self.form()
        search_term = self.request.GET.get('q', '').strip()
        categories = Category.objects.filter(
            Q(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term),
            )
        ).order_by('-id')

        current_page = int(request.GET.get('page', 1))
        paginator = Paginator(categories, per_page=10)
        page_obj = paginator.get_page(current_page)

        pagination_range = make_pagination_range(
            page_range=paginator.page_range,
            qty_pages=4,
            current_page=current_page,
        )

        if not search_term:
            raise Http404()

        context = {
            'form': form,
            'categories': page_obj,
            'pagination_range': pagination_range,
            'search_term': search_term,
            'additional_url_query': f'&q={search_term}',
        }

        return render(request, self.template_name, context=context)


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class CategoryUpdateView(SuccessMessageMixin, generic.UpdateView):
    model = Category
    fields = ["name", "description"]
    template_name = 'dashboard/partials/category/category_table_update_modal.html'  # noqa
    success_message = 'Category updated successfully'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        _id = int(self.kwargs.get('pk'))
        category = get_object_or_404(Category, pk=_id)
        return category

    def get_success_url(self):
        return reverse_lazy('dashboard:leads_category')


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class CategoryDeleteView(SuccessMessageMixin, generic.DeleteView):
    template_name = 'dashboard/partials/category/category_table_delete_modal.html'  # noqa
    success_message = 'Category deleted successfully'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        _id = int(self.kwargs.get('pk'))
        category = get_object_or_404(Category, pk=_id)
        return category

    def get_success_url(self):
        return reverse_lazy('dashboard:leads_category')


@method_decorator(
    login_required(
        login_url='users:login',
        redirect_field_name='next'
    ),
    name='dispatch'
)
class CategoryExportView(generic.View):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def setup(self, *args, **kwargs):
        return super().setup(*args, **kwargs)

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        categories = Category.objects.all().order_by('-id')
        data = []

        for category in categories:
            data.append({
                'name': category.name,
                'description': category.description
            })

        messages.success(request, 'Category export successfully')
        pandas.DataFrame(data).to_excel('categories.xlsx')

        return redirect('dashboard:leads_category')
