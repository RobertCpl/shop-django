from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def products(request):
    return HttpResponse("Products page")
def product_detail(request, product_slug):
    return HttpResponse("You're looking at product %s." % product_slug)