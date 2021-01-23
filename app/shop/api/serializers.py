# from django.contrib.auth.models import User
# from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from shop.models import Address, Cart, Product, Order

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        # fields = ('email', 'password',)
        fields = ('name', 'email', 'password', 'addresses','carts')

        write_only_fields = ('password',)

    def restore_object(self, attrs, instance=None):
        user = self.restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id','user','first_name','last_name','street_address1','street_address2', 'city', 'state', 'phone',)


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ( 'url', 'items','user')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ( 'url', 'product_name','category','status', 'our_price', 'original_price','image_url','origianl_url', 'html','options' )

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ( 'url', 'items','cart')

class AuditSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('name', 'email', 'password', 'addresses','carts')
        write_only_fields = ('password',)
        depth = 3