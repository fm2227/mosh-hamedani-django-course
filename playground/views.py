from django.shortcuts import render
from django.db.models import Q, Func
from django.db.models import Value, F, ExpressionWrapper, DecimalField
from django.db.models.functions import Concat
from django.db.models.aggregates import Min, Max, Count, Sum, Avg
from store.models import Product, Collection, OrderItem, Order, Customer


def say_hello(request):
    discounted_price = ExpressionWrapper(
        F('unit_price') * 0.8, output_field=DecimalField())
    queryset = Product.objects.annotate(discounted_price=discounted_price)
    return render(request, 'playground/hello.html', {'name': 'farshad', 'result': queryset})
