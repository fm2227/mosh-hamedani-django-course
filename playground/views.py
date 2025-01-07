from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from store.models import Product
from tags.models import TagItem


def say_hello(request):
    queryset = TagItem.objects.get_tags_for(Product, 1)
    return render(request, 'playground/hello.html', {'name': 'farshad', 'result': queryset})
