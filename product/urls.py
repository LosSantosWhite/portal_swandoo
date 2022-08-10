from django.urls import path

from product.views import ProductListView, ProductDetailView

app_name = 'product'

urlpatterns = [
    path('all-products/', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]