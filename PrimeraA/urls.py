from django.conf.urls import url, include
from rest_framework import routers
from PrimeraA import views


urlpatterns = [
    url(r'^equipos/$', views.equipo_list),
    url (r'^equipos/(?P<pk>[0-9]+)/$', views.equipo_detail),

]