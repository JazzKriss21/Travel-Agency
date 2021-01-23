from rest_framework.serializers import ModelSerializer
from crowdfund.models import Fundraiser

class FundraiserSerializer(ModelSerializer):
    class Meta:
        model = Fundraiser
        fields = ('id','user','title','description','date_created','date_goal','amount_funded','amount_goal','date_created')


#   user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="fundraiser", on_delete=models.CASCADE)
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     date_created = models.DateField(auto_now=True)
#     date_goal = models.DateField(validators=[validate_date_goal])
#     date_finished = models.DateField(null=True, blank=True)
#     status = models.PositiveSmallIntegerField(default=1, choices=STATUS_CHOICES)
#     amount_funded = models.FloatField(default=0)
#     amount_goal = models.FloatField(validators=[validate_amount_goal])