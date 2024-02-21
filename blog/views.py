from django.views import generic
from .models import Category

class CategoricalView(generic.ListView):
    model = Category
    template_name = 'blog/categories.html'
    context_object_name = 'categories'