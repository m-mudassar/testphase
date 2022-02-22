import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from ecom import models
from ecom import models
from ecom.models import Vehicle

def getVehicles():
    vehicle = Vehicle.objects.all() 
    args = {'vehicles': vehicle}
    return args
# Create your views here.
def index(request):
   return render(request, 'index.html', getVehicles())

def add(request):
    if request.method == "POST":
        vehicleNo = request.POST["vehicle-no"]
        brand = request.POST["brand"]
        model = request.POST["model"]
        vehicle = Vehicle(vehicleNo=vehicleNo, brand=brand, model=model)
        vehicle.save()
        print("data is going to database")
    return render(request, 'index.html', getVehicles())

def delete(request):
    if request.method == "POST":
        vehicleid = request.POST["vehicleNo"]
        print("post is working")
        print(vehicleid) 
        instance = Vehicle.objects.get(vehicleNo=vehicleid)
        print("deleteis working")
        instance.delete()
    return render(request, 'index.html', getVehicles())
