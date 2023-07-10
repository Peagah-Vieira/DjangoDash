from django.shortcuts import render, redirect
from django.views import generic
from .forms import CategoryForm
from django.urls import reverse_lazy
from django.contrib import messages
from leads.models import Category
from django.shortcuts import get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin


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


class CategoryView(generic.CreateView):
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
        context = {'form': form, 'categories': categories}
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


class CategoryDeleteView(SuccessMessageMixin, generic.DeleteView):
    template_name = 'dashboard/partials/category/category_table_delete_modal.html'  # noqa
    success_message = 'Category deleted successfully'

    def get_object(self):
        _id = int(self.kwargs.get('pk'))
        category = get_object_or_404(Category, pk=_id)
        return category

    def get_success_url(self):
        return reverse_lazy('dashboard:leads_category')
