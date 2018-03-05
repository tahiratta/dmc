from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^$', views.logo, name='logo'),
	url(r'^home/', views.home, name='home'),
	url(r'^blog/', views.blog, name='blog'),
	url(r'^blog-single/', views.blogSingle, name='blog-single'),
	url(r'^service-list/', views.serviceList, name='service-list'),
	url(r'^service-detail/', views.serviceDetail, name='service-detail'),
	url(r'^contact-us/', views.contact, name='contact-us'),
	url(r'^style-guide/', views.styleGuide, name='style-guide'),
]

