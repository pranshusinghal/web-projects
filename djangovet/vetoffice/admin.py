from django.contrib import admin
from .models import Owner, Patient, Appointment

admin.site.register(Owner)
admin.site.register(Patient)
admin.site.register(Appointment)