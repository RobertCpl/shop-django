# 
from django.urls import path
from . import views


urlpatterns = [
    path('products/', views.products, name='show_products'),
    path('products/<product_slug>/', views.product_detail, name='product_detail'),
]