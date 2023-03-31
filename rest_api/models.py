from django.db import models


class Record(models.Model):
    date = models.DateField()
    lat = models.FloatField()
    lon = models.FloatField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    temperature = models.FloatField()

    class Meta:
        ordering = ['id']

        
class Temp(models.Model):
     date = models.DateField()
     lat = models.FloatField()
     lon = models.FloatField()
     city = models.CharField(max_length=255)
     state = models.CharField(max_length=255)
     temperature = models.FloatField()

     class Meta:
        ordering = ['id']
    
