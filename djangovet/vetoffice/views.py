from django.shortcuts import render
from .models import Owner, Patient
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.http import Http404

def home(request):
  try:
    found_pet = Patient.objects.get(pk=1)
  except Patient.DoesNotExist:
    raise Http404()
  context = {"name": "Djangoer", "pet": found_pet}
  return render(request, "vetoffice/home.html", context)

class OwnerList(ListView):
  model = Owner
  template_name = "vetoffice/owner_list.html"

class PatientList(ListView):
  model = Patient
  template_name = "vetoffice/patient_list.html"

class OwnerCreate(CreateView):
  model = Owner
  template_name = "vetoffice/owner_create_form.html"
  fields = ["first_name", "last_name", "phone"]
  success_url = "/vetoffice/owner/list"

class PatientCreate(CreateView):
  model = Patient
  template_name = "vetoffice/patient_create_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]
  success_url = "/vetoffice/patient/list"

class OwnerUpdate(UpdateView):
  model = Owner
  template_name = "vetoffice/owner_update_form.html"
  fields = ["first_name", "last_name", "phone"]
  success_url = "/vetoffice/owner/list"

class PatientUpdate(UpdateView):
  model = Patient
  template_name = "vetoffice/patient_update_form.html"
  fields = ["animal_type", "breed", "pet_name", "age", "owner"]
  success_url = "/vetoffice/patient/list"

class OwnerDelete(DeleteView):
  model = Owner
  template_name = "vetoffice/owner_delete_form.html"
  success_url = "/vetoffice/owner/list"

class PatientDelete(DeleteView):
  model = Patient
  template_name = "vetoffice/patient_delete_form.html"
  success_url = "/vetoffice/patient/list"