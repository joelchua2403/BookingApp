from django.db import models



# Create your models here.
class Date(models.Model):
    date = models.TextField(null=True, blank=True)
    time = models.TextField(null=True, blank=True)
    


class Booking(models.Model):
    vesselName = models.CharField(max_length=50)
    berth = models.CharField(max_length=254)
    date_time = models.ForeignKey(Date, on_delete=models.CASCADE, null=True, blank=True, default=None)
    activity = models.TextField(null=True, blank=True)
    pilot = models.CharField(max_length=254, null=True, blank=True)
    tug = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   


   