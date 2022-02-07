from django.db import models
from django.utils import timezone


# Create your models here.
class Shelter(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    foster_program = models.BooleanField()
    city = models.CharField(max_length=50)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Pet(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    adoptable = models.BooleanField()
    age = models.IntegerField()
    breed = models.CharField(max_length=50)
    name = models.CharField(max_length=255)


class VeterinaryOffice(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    boarding_services = models.BooleanField()
    max_patient_capacity = models.IntegerField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Veterinarian(models.Model):
    veterinary_office = models.ForeignKey(VeterinaryOffice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    on_call = models.BooleanField()
    review_rating = models.IntegerField()
    name = models.CharField(max_length=255)
