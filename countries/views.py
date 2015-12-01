from django.shortcuts import render
from .models import Country

def country(request):
	return render(request, "country.html", {"country": Country.objects.all()})