# -*- coding: ISO-8859-1 -*-

from django.conf.urls import patterns, url, include
from apps.main import views

urlpatterns = patterns('',
	url(r'^$', views.home, name="home"),
)

