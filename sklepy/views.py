from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.forms import modelform_factory


def index(request):
    form = modelform_factory(ShoppingPosition, fields='__all__')
    isAdded = False
    if request.method == 'POST':
        formset = form(request.POST, request.FILES)
        formset.save()
        isAdded = True

    return render(request, 'sklepy/index.html', {'isAdded': isAdded})


def formularz(request):
    form = modelform_factory(ShoppingPosition, fields='__all__')
    return render(request, 'sklepy/formularz.html', {'formset': form})


def widok(request):
    sklepy = Shop.objects.order_by('shop_name', )
    lista = ShoppingPosition.objects.order_by('-shop', )

    actual = []
    for i in lista:
        if i.shop.shop_name not in actual:
            actual.append(i.shop.shop_name)

    prices = []
    for i in sklepy:
        temp = 0
        for j in lista:
            if i.shop_name == j.shop.shop_name:
                temp += (j.product_count * j.product.product_price)
        if temp != 0:
            prices.append(temp)

    prices.reverse()

    return render(request, 'sklepy/widok.html', {'lista': lista,
                                                 'sklepy': sklepy,
                                                 'validator': actual,
                                                 'prices': prices})
