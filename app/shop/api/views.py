# from django.contrib.auth.models import User
# from django.conf import settings
from django.contrib.auth import get_user_model
from accounts_api.models import UserProfile
# from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import AccountSerializer, AddressSerializer, CartSerializer, ProductSerializer, OrderSerializer, AuditSerializer
from shop.models import Address, Cart, Product, Order



class AccountViewSet(viewsets.ModelViewSet):
    model = get_user_model()
    serializer_class = AccountSerializer
    permission_classes = ()

    def post_save(self, obj, created=False):
        if created:
            cart = Cart(user=obj)
            cart.save()

    def get_queryset(self,):
        user = self.request.user
        return UserProfile.objects.filter(pk=user.pk)



class AddressViewSet(viewsets.ModelViewSet):
    model = Address
    serializer_class = AddressSerializer

    def get_queryset(self,):
        user = self.request.user
        return Address.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self,):
        return Cart.objects.filter(user=self.request.user)

    # @action()
    def add(self, request, pk):
        '''
            create product and add it to the cart represented by pk
        '''
        return Response({"success":True})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self,):
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailedAccountViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = AuditSerializer
    permission_classes = (IsAdminUser,)