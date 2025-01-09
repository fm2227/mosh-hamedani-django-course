from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Order, OrderItem, Customer, Product
from tags.models import TagItem
from django.db import transaction


def say_hello(request):

    with transaction.atomic():
        order = Order()
        order.Customer_id = 1
        order.save()

        item = OrderItem()
        item.order = order
        item.product_id = -1
        item.quantity = 1
        item.unit_price = 10
        item.save()
    return render(request, 'playground/hello.html', {'name': 'farshad', })
