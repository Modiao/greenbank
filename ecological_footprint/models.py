from typing import Any
from django.db import models
from django.core.exceptions import ValidationError


# Create your models here.

def validate_mileage(value):
    if value not in range(5000, 30000):
        raise ValidationError("veuillez choisir un mileage qui est dans l'interval [5000, 30000]")

def validate_year(value):
    if int(value) < 1960:
        raise ValidationError("veuillez une année supérieure ou égale à 1960")
        
def validate_passenger(value):
    if value not in range (1, 5):
        raise ValidationError("veuillez choisir un nombre compris en 1 et 4")


class InfosVehiculeFoyer(models.Model):

    CITADINE = 'Citadine'
    CABRIOLET = 'Cabriolet'
    BERLINE = 'Berline'
    SUV_4_4 = 'SUV / 4x4'

    VEHICULE_TYPE = [
        (CITADINE, 'Citadine'),
        (CABRIOLET, 'Cabriolet'),
        (BERLINE, 'Berline'),
        (SUV_4_4, 'SUV / 4x4')
    ]

    ESSENCE = 'Essence'
    ELECTRIQUE = 'Electrique'
    GAZ = 'Gaz'
    DIESEL = 'Diesel'
    HYBRIDE = 'Hybride'

    ENERGY_TYPE = [
        (ESSENCE, 'Essence'),
        (ELECTRIQUE, 'Electrique'),
        (GAZ, 'Gaz'),
        (DIESEL, 'Diesel'),
        (HYBRIDE, 'Hybride')
    ]



    type_vehicule = models.CharField(max_length=20, choices=VEHICULE_TYPE)
    energy = models.CharField(max_length=20, choices=ENERGY_TYPE)
    mileage = models.IntegerField(validators=[validate_mileage])
    year = models.IntegerField(validators=[validate_year])
    passenger =  models.IntegerField(validators=[validate_passenger])
    borrowing_rate = models.FloatField(default=0.0)


    def __str__(self):
        return f"{self.type_vehicule} - {self.energy} - {self.mileage} - {self.year} - {self.passenger} - {self.borrowing_rate}"
    
  