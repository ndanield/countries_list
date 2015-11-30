from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /country/
	url(r'^$', views.country, name='country')
]