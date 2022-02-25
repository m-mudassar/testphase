import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from ecom import models
from ecom import models
from ecom.models import Vehicle, Service

args = None


def getVehicles():
    vehicle = Vehicle.objects.all()
    args = {'vehicles': vehicle}
    return args


def getServices():
    global args
    return args
# Create your views here.


def index(request):
    return render(request, 'index.html', getServices())


def add(request):
    if request.method == "POST":
        vehicleNo = request.POST["vehicle-no"]
        brand = request.POST["brand"]
        model = request.POST["model"]
        vehicle = Vehicle(vehicleNo=vehicleNo, brand=brand, model=model)
        vehicle.save()
        print("data is going to database")
        global args
        args = None
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
        vehicle_no = request.POST["vehicle-no"]
        vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)
        service = Service.objects.filter(vehicleNo=vehicle)

        print("vehicle in search")
        print(vehicle)
        print("service in search")
        print(service)
        print("search is working")

        global args
        args = {'services': service, 'vehicle': vehicle}
        return render(request, 'search.html', {'request': 'ok'})
    return render(request, 'search.html')


def add_service(request):
    if request.method == "POST":
        vehicle_no = request.POST["vehicle-no"]
        service_id = request.POST["service_id"]
        service_type = request.POST["service_type"]
        vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)

        print("in add service vehicle")

        service = Service(serviceID=service_id,
                          service_type=service_type, vehicleNo=vehicle)
        service.save()

        service = Service.objects.filter(vehicleNo=vehicle)

        global args
        args = {'services': service, 'vehicle': vehicle}

        print(vehicle_no, service_id, service_type)
    return render(request, 'add_service.html')


def update_service(request):
    return 0


def delete_service(request):
    return 0
