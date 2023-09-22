from django.test import TestCase
from apps.weather import models

class TestLocationModel(TestCase):
    def setUp(self):
        self.city_name = "Hamburg"
        self.country_name = "Germany"
        self.lat_= "12.2565.65"
        self.long_= '254.2555.221'
        self.location = models.Location(
            city = self.city_name,
            country = self.country_name,
            lat = self.lat_,
            long = self.long_
        )

    def test_create_location_object_successful(self):
        self.assertIsInstance(self.location, models.Location)

    def test_dunder_str(self):
       #str(self.tag) or self.tag.__str__()
        self.assertEqual(str(self.location), f"{self.country_name},{self.city_name}")
        