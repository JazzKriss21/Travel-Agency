from django.db import models


class FlightDetails(models.Model):
    originCitiesChoices = (
        ('MAA', 'Chennai'),
        ('DEL', 'DELHI'),
        ('BLR', 'Bengaluru'),
        ('CCU', 'Kolkata'),
        ('HYD', 'Hyderabad'),

    )
    destinationCitiesChoices = (
        ('MAA', 'Chennai'),
        ('DEL', 'DELHI'),
        ('BLR', 'Bengaluru'),
        ('CCU', 'Kolkata'),
        ('HYD', 'Hyderabad'),

    )
    originCity = models.CharField(max_length=20, choices=originCitiesChoices)
    destinationCity = models.CharField(max_length=20, choices=destinationCitiesChoices)
    Departure_date = models.DateField(blank=False)
    Return_date = models.DateField(blank=False)
    adults = models.CharField(max_length=10)
    members = models.CharField(max_length=10)
    classChoices = (
        ('1', 'A'),
        ('2', 'B'),
        ('3', 'C'),
    )
    classType = models.CharField(max_length=1, choices=classChoices)
