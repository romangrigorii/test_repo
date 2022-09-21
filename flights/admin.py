from ast import Pass
from django.contrib import admin

from .models import flight, airport, passenger

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id","origin","destination","duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(airport)
admin.site.register(flight, FlightAdmin)
admin.site.register(passenger,PassengerAdmin)



# Register your models here.
