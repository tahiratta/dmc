from django.conf.urls import url
from . import views

from dmc import views as dmc_views 

urlpatterns = [
	url(r'^$', dmc_views.index, name='index'),
]

