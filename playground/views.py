from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Order, OrderItem, Customer, Product
from tags.models import TagItem
from django.db import transaction


def say_hello(request):
    queryset = Product.objects.raw('SELECT id,title FROM store_product')
    return render(request, 'playground/hello.html', {'name': 'farshad', 'result': list(queryset)})
