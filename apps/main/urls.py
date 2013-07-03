# -*- coding: ISO-8859-1 -*-

from django.conf.urls import patterns, url, include
from apps.main import views

from django.conf.urls import patterns, url, include
from django.contrib.auth.forms import AuthenticationForm

urlpatterns = patterns('',
	url(r'^$', views.home, name="home"),
	url(r'^login/?$', 'django.contrib.auth.views.login',  {'template_name':'main/auth/login.html', 'authentication_form': AuthenticationForm}),
	url(r'^logout/?$', views.logout, name="logout"),
	url(r'^clientes/?$', views.clientes, name="clientes"),
	url(r'^consumos/?$', views.consumos, name="consumos"),
	url(r'^cliente/(?P<pk>[^/]+)/$',views.cliente, name="cliente"),
	url(r'^operarios/?$',views.operarios, name="operarios"),
	url(r'^operario/(?P<pk>[^/]+)/$',views.operario, name="operario")
)

