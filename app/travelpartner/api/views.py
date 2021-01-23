from django.contrib.auth import get_user_model
from accounts_api.models import UserProfile
# from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import TravelPartnerSerializer
from travelpartner.models import TravelPartner 

class TravelPartnerViewSet(viewsets.ModelViewSet):
    model = TravelPartner
    serializer_class = TravelPartnerSerializer

    def get_queryset(self,):
        user = self.request.user
        return TravelPartner.objects.filter(user=user)

    def perform_create(self, serializer):
        user=self.request.user
        serializer.save(user=user, name=user.name)