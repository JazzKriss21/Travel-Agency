from datetime import datetime
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.forms import ModelForm

STATUS_CHOICES = ((1, 'Ongoing'), (2, 'Completed'), (3, 'Ended'))

def validate_date_goal(value):
    now = datetime.now().date()
    if value and (value - now).days < 1:
        raise ValidationError('Goal date should be at least 1 day from now')


def validate_amount_goal(value):
    if not value or value < 0:
        raise ValidationError('Goal amount should be greater than 0')


class Fundraiser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="fundraiser", on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="travelpartner", on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    number = models.CharField(max_length=200)

    description = models.TextField()
    date_created = models.DateField(auto_now=True)
    date_goal = models.DateField(validators=[validate_date_goal])
    # date_finished = models.DateField(null=True, blank=True)
    # status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)
    amount_funded = models.FloatField(default=0)
    amount_goal = models.FloatField(validators=[validate_amount_goal])

    def __str__(self):
        return self.title

class FundraiserFormModel(ModelForm):
    class Meta:
        model = Fundraiser
        # fields =['user','title','description','date_goal','date_finished','amount_funded','amount_goal',]
        fields ='__all__'
        exclude = ['user','amount_funded']


    