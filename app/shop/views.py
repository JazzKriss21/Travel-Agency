from django.shortcuts import render
from shop.api.serializers import AccountSerializer, AddressSerializer, CartSerializer, ProductSerializer, OrderSerializer, AuditSerializer
from shop.models import Address, Cart, Product, Order
# Create your views here.

# Create your views here.
def product_view(request):
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset,context={'request':request},many=True)
    data = {
        "test": serializer.data
    }
    return render(request, "shop.html",data)

def cart_view(request):
    return render(request, "cart.html")

def product_detail(request):
    return render(request, "productdetail.html")