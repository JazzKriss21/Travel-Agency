from rest_framework import serializers
# from django.contrib.auth import get_user_model
from travelpartner.models import TravelPartner

class TravelPartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelPartner
        # fields = ( 'url', 'user','name','start_date', 'end_date', 'original_price','image_url','origianl_url', 'html','options' )
        fields = ('url', 'user', 'name', 'start_date', 'end_date', 'destination', 'description', 'phone')

