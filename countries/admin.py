from django.contrib import admin
from .models import Country

class CountryAdmin(admin.ModelAdmin):
	list_display = ['code', 'name', 'continent', 'region', 'population']
	
admin.site.register(Country, CountryAdmin)