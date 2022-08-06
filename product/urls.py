from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('products/add/',views.product_insert,name="product-insert"),
    path('category/add/',views.category_insert,name="category-insert"),
    path('products/',views.product_list,name="product-list"),
    path("product/<slug:slug>/",views.product_detail, name="product-detail")
    
]