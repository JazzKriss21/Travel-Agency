# from django.contrib.auth.models import User
from django.conf import settings
from django.db import models


class Address(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="addresses", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address1 = models.CharField(max_length=255)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)


CATEGORY_CHOICES = ((1, 'Electronics'), (2, 'Apparels'), (3, 'Bags'),
                    (4, 'Miscellaneous'), (5, 'All'))

class Product(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    category = models.PositiveSmallIntegerField(choices=CATEGORY_CHOICES, default=5)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    our_price = models.DecimalField(max_digits=10, decimal_places=2)
    origianl_url = models.TextField()
    image_url = models.TextField()
    html = models.TextField()
    options = models.TextField()
    imageData = models.TextField()

 
class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="carts", on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)    


class Order(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    cart = models.ForeignKey(Cart, blank=True, null=True, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="orders", on_delete=models.CASCADE)