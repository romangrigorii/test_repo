from django.test import TestCase, Client
from .models import *
from django.db.models import *

# Create your tests here.

class FlightTestCase(TestCase):

    # The code below tests specific structures inside the models.py

    def setUp(self):

        a1 = airport.objects.create(code  = "AAA", city = "City A")
        a2 = airport.objects.create(code  = "BBB", city = "City B")

        flight.objects.create(origin = a1, destination = a2, duration = 100)
        flight.objects.create(origin = a1, destination = a1, duration = 200)
        flight.objects.create(origin = a2, destination = a2, duration = -100)

    def test_departures_count(self):
         a = airport.objects.get(code = "AAA")
         self.assertEqual(a.departures.count(),2)

    def test_arrivals_count(self):
        a = airport.objects.get(code = "AAA")
        self.assertEqual(a.arrivals.count(),1)

    def test_valid_flight(self):
        a1 = airport.objects.get(code="AAA")
        a2 = airport.objects.get(code="BBB")
        f = flight.objects.get(origin = a1, destination = a2, duration = 100)
        self.assertTrue(f.is_valid_flight())
    
    def test_invalid_flight_destination(self):
        a1 = airport.objects.get(code="AAA")
        f = flight.objects.get(origin = a1, destination = a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        a1 = airport.objects.get(code="AAA")
        a2 = airport.objects.get(code="BBB")
        f = flight.objects.get(origin = a2, destination = a2, duration = -100)
        self.assertFalse(f.is_valid_flight())

    # The code below will test specific webpages on the server

    def test_index(self):
        c = Client()
        response = c.get("/flights/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(),3) # make sure there are exactly 3 results

    def test_valid_flight_page(self):
        a1 = airport.objects.get(code = "AAA")
        f = flight.objects.get(origin = a1, destination = a1)
        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code,200)

    # def test_invalid_flight_page(self):
    #     max_id = flight.objects.all().aggregate(Max("id"))["id__max"]
    #     c = Client()
    #     response = c.get(f"/flights/{max_id+1}")
    #     self.assertEqual(response.status_code,404)

    def test_flight_page_passengers(self):
        f = flight.objects.get(pk = 1)
        p = passenger.objects.create(first = "Alice", last = "Adams")
        f.passengers.add(p)

        c = Client()
        response = c.get(f"/flights/{f.id}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["passengers"].count(),1)

    # The code below will test browser functionality directly

    
    
    


        