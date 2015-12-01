from django.shortcuts import render
from .models import Country
from django_tables2 import RequestConfig
from .tables import CountryTable

def country(request):
	#"country": Country.objects.all()
	table = CountryTable(Country.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'country.html', {'table': table})