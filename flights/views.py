from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import * # urls imports views and views imports models. urls go to urls that views generate with data from models.

def index(request):
    return render(request,"flights/index.html",{
        "flights": flight.objects.all()
    })

def flightfunction(request, flight_id):
    Flight = flight.objects.get(pk=flight_id)
    return render(request, "flights/flight.html", {
        "Flight" : Flight,
        "passengers" : Flight.passengers.all(),
        "non_passengers" : passenger.objects.exclude(flights=Flight).all(),
    }) 

def book(request, flight_id):    
    if request.method == "POST":
        Flight = flight.objects.get(id=flight_id)
        Passenger = passenger.objects.get(id=int(request.POST["passenger"]))
        Passenger.flights.add(Flight)
        return HttpResponseRedirect(reverse("flights:Flight", args = (Flight.id,)))
    return HttpResponseRedirect(reverse("flights:index"))