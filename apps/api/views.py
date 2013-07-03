# Create your views here.
#!--coding:utf-8--#

from apps.main.models import *
from apps.api.serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view, action , link

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
from django.utils.timezone import utc
from django.core import serializers


#============================================================
# CONSUMO VIEW SET
#============================================================

class ConsumoViewSet(viewsets.ModelViewSet):
	"""
	A viewset that provides the standard actions 
	"""
	queryset = Consumo.objects.all()
	serializer_class = ConsumoSerializer

#============================================================
# CLIENTE VIEW SET
#============================================================

class ClienteViewSet(viewsets.ModelViewSet):
	"""
	A viewset that provides the standard actions 
	"""
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

#============================================================
# OPERARIO VIEW SET
#============================================================

class OperarioViewSet(viewsets.ModelViewSet):
	"""
	A viewset that provides the standard actions 
	"""
	queryset = Operario.objects.all()
	serializer_class = OperarioSerializer