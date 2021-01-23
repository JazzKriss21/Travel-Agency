from django.urls import path, include
from shop import  views

urlpatterns = [
    path('api/', include('shop.api.urls')),
    path('products/',views.product_view),
    path('products/detail', views.product_detail),

    path('products/cart/', views.cart_view,name='cart'),
]
