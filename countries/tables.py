import django_tables2 as tables
from .models import Country

class CountryTable(tables.Table):
    class Meta:
        model = Country
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue"}