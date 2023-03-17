from django.shortcuts import render
from django.http import HttpResponse


def home(request):
  context = {"name": "Spot"}
  return render(request, "vetoffice/home.html", context)