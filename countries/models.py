from django.db import models

# class language(models.Model):
	# countrycode = models.ForeignKey(Country)
	# name = models.CharField(max_length=25)
	# isofficial = models.BooleanField()
	# percentage = models.DecimalField(max_digits=3, decimal_places=1)

class Country(models.Model):
	code = models.CharField(max_length = 3)
	name = models.CharField(max_length = 46)
	continent = models.CharField(max_length=20)
	region = models.CharField(max_length = 30)
	population = models.IntegerField()