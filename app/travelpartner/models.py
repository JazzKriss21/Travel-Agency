from django.conf import settings
from django.db import models


class TravelPartner(models.Model):

    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="travelpartner", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)
    destination = models.CharField(max_length=255)
    description = models.TextField()
    phone = models.CharField(max_length=255, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('partners-detail', args=[self.id])

    def __str__(self):
        return self.name

    # class TravelPartner(models.Model):
