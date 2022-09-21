from django.urls import path

from . import views

app_name = "flights"

urlpatterns = [
    path("", views.index,name = "index"), # name allows references uing {% url %}, views.index refenreces the function that will deal with this call
    path("<int:flight_id>", views.flightfunction, name = "Flight"), 
    path("<int:flight_id>/book", views.book, name = "book")
]

