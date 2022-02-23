import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
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
    return redirect('/')

def delete(request):
    if request.method == "POST":
        vehicleid = request.POST["vehicleNo"]
        print(vehicleid) 
        instance = Vehicle.objects.get(vehicleNo=vehicleid)
        print("delete is working")
        instance.delete()
    return redirect('/')

def search(request):
    if request.method == "POST":
        print("search is working")
        render(request, 'index.html')
    return render(request, 'search.html')