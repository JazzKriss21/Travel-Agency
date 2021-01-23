from .models import TravelPartner
from django.forms import ModelForm

class TravelPartnerForm(ModelForm):
    class Meta:
        model=TravelPartner
        fields='__all__'
        exclude=['user']
0