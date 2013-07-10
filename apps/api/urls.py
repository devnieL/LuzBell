#!--coding:utf-8--#

from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
admin.autodiscover()
import views

urlpatterns = patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^login/$', views.UserLogin.as_view()),
    url(r'^consumos/add/$', views.RegistroConsumo.as_view()),
)

router = routers.DefaultRouter()
router.register(r'clientes', views.ClienteViewSet)
router.register(r'operarios', views.OperarioViewSet)
router.register(r'consumos', views.ConsumoViewSet)

urlpatterns += router.urls