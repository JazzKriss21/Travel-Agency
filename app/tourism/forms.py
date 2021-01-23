from .models import FlightDetails
from django.forms import ModelForm

class FlightDetailsForm(ModelForm):
    class Meta:
        model=FlightDetails
        fields='__all__'
