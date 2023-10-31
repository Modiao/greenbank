from django.test import TestCase
import unittest

# Create your tests here.import unittest
from django.core.exceptions import ValidationError
from .models import InfosVehiculeFoyer

class TestInfosVehiculeFoyerModel(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            'type_vehicule': InfosVehiculeFoyer.CITADINE,
            'energy': InfosVehiculeFoyer.ESSENCE,
            'mileage': 7500,
            'year': 1980,
            'passenger': 2,
        }

    def test_valid_data(self):
        instance = InfosVehiculeFoyer(**self.valid_data)
        self.assertIsNone(instance.full_clean())  # Should not raise ValidationError

    def test_invalid_mileage(self):
        invalid_data = self.valid_data.copy()
        invalid_data['mileage'] = 4000  # Below the valid range
        instance = InfosVehiculeFoyer(**invalid_data)
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def test_invalid_year(self):
        invalid_data = self.valid_data.copy()
        invalid_data['year'] = 1950  # Below the valid range
        instance = InfosVehiculeFoyer(**invalid_data)
        with self.assertRaises(ValidationError):
            instance.full_clean()

    def test_invalid_passenger(self):
        invalid_data = self.valid_data.copy()
        invalid_data['passenger'] = 5  # Above the valid range
        instance = InfosVehiculeFoyer(**invalid_data)
        with self.assertRaises(ValidationError):
            instance.full_clean()

if __name__ == '__main__':
    unittest.main()
