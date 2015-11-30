from django.shortcuts import render
from .models import Country

def country(request):
	return render(request, 'countries/country.html', {"country": Country.objects.all()})