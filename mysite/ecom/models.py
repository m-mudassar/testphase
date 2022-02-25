from django.db import models

# Create your models here.
class Vehicle(models.Model):
    vehicleNo = models.CharField(max_length=12, primary_key=True)
    brand = models.CharField(max_length=25)
    model = models.CharField(max_length=12)

class Service(models.Model):
    serviceID = models.IntegerField(primary_key=True, default=0)
    service_type = models.CharField(max_length=10, default="null")
    vehicleNo = models.ForeignKey(Vehicle, on_delete=models.CASCADE)