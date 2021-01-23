# from django.shortcuts import render
from rest_framework import viewsets
from crowdfund.models import Fundraiser
from .serializers import FundraiserSerializer


class FundraiserViewSet(viewsets.ModelViewSet):
  
    queryset = Fundraiser.objects.all()
    serializer_class = FundraiserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)