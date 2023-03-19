from django.db import models

"""
Owner instance can have multiple Patients — and Patients can only have one Owner. 
In code, that means the Patient needs a foreign key of an Owner.
"""
class Owner(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  phone = models.CharField(max_length=30)
  
  def __str__(self):
    return self.first_name + " " + self.last_name

  def has_multiple_pets(self):
    # using "Reverse Relationship" concept to get patients count
    return self.patient_set.count() > 1


class Patient(models.Model):
  DOG = "DO"
  CAT = "CA"
  BIRD = "BI"
  REPTILE = "RE"
  OTHER = "OT"
  ANIMAL_TYPE_CHOICES = [
    (DOG, "Dog"),
    (CAT, "Cat"),
    (BIRD, "Bird"),
    (REPTILE, "Reptile"),
    (OTHER, "Other"),
  ]
  animal_type = models.CharField(max_length=2, choices=ANIMAL_TYPE_CHOICES, default=OTHER)
  breed = models.CharField(max_length=200)
  pet_name = models.CharField(max_length=200)
  age = models.IntegerField(default=0)
  owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.pet_name + ", " + self.animal_type

  class Meta:
    ordering = ["pet_name"]

