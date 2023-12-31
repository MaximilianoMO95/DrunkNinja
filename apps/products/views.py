from django.contrib.admin.options import HttpResponseRedirect, method_decorator
from django.contrib.auth.views import login_required
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView

from .models import (Product, Category, Basket)

class IndexView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductsListView(ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 3
    ordering = ['name']

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category=category_id) if category_id else queryset

    def get_context_data(self, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = Category.objects.all()
        return context


@method_decorator(login_required, name='dispatch')
class BasketView(TemplateView):
    template_name = 'products/basket.html'

    def get_context_data(self, **kwargs):
        basket_items = Basket.objects.filter(user=self.request.user)

        total_sum = basket_items.total_sum()
        total_quantity = basket_items.total_quantity()

        context = {
            'basket_items': basket_items,
            'total_sum': total_sum,
            'total_quantity': total_quantity,
        }

        return context


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(product_id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
