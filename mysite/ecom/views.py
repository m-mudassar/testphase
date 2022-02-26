import re
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from ecom import models
from ecom import models
from ecom.models import Vehicle, Service
from django.core.exceptions import ObjectDoesNotExist

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

        global args
        args = None
        
    return redirect('/')


def delete(request):
    if request.method == "POST":
        vehicle_no = request.POST["vehicle-no"]
        vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)
        vehicle.delete()

        global args
        args = None

        return render(request, 'delete.html', {'request': 'ok'})
    return render(request, 'delete.html')


def search(request):
    if request.method == "POST":
        vehicle_no = request.POST["vehicle-no"]

        try:
            vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)
            service = Service.objects.filter(vehicleNo=vehicle)
            global args
            args = {'services': service, 'vehicle': vehicle}
        except ObjectDoesNotExist:
            return render(request, 'search.html', {'request': 'Record not found'})

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
    if request.method == "POST":
        vehicle_no = request.POST["vehicle-no"]
        vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)
        vehicle.delete()
        print("delete success")
        return render(request, 'delete.html', {'request': 'ok'})
    return render(request, 'delete.html')


def delete_service(request):
    if request.method == "GET":
        vehicle_no = request.GET["vehicleid"]
        service_id = request.GET["serviceid"]
        print(vehicle_no, service_id)
        try:
            vehicle = Vehicle.objects.get(vehicleNo=vehicle_no)
            service = Service.objects.filter(serviceID=service_id)
            service.delete()            
            services = Service.objects.filter(vehicleNo=vehicle)
            global args
            args = {'services': services, 'vehicle': vehicle}
        except ObjectDoesNotExist:
            return redirect('/')

        return redirect('/')
    return redirect('/')
