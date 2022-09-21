from django.db import models

# Create your models here.

class airport(models.Model):
    code = models.CharField(max_length = 3)
    city = models.CharField(max_length = 64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class flight(models.Model):
    origin = models.ForeignKey(airport, on_delete=models.CASCADE, related_name = "departures")
    destination = models.ForeignKey(airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.id} : {self.origin} to {self.destination}"

    def is_valid_flight(self):
        return self.destination!=self.origin and self.duration>0

class passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(flight, blank = True, related_name="passengers") # ManyToManyField allows us to reference multiple flights to one passenger and vice versa # related name will act as a token that allows for this.

    def __str__(self):
        return f"{self.first} {self.last}"