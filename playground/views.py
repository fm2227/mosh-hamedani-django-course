from django.shortcuts import render
from django.db.models import Q, F, Func
from django.db.models import Value
from django.db.models.functions import Concat
from django.db.models.aggregates import Min, Max, Count, Sum, Avg
from store.models import Product, Collection, OrderItem, Order, Customer


def say_hello(request):
    queryset = Customer.objects.annotate(
        orders_count=Count('order')
    )
    return render(request, 'playground/hello.html', {'name': 'farshad', 'result': queryset})
