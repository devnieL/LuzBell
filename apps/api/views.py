# Create your views here.
#!--coding:utf-8--#

from apps.main.models import *
from apps.api.serializers import *
from rest_framework import viewsets
from rest_framework.decorators import api_view, action , link

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions

from datetime import datetime
from datetime import time
from datetime import date
from datetime import timedelta
from django.utils.timezone import utc
from django.core import serializers

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login



#============================================================
# CONSUMO
#============================================================

class RegistroConsumo(APIView):

	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):

		data = request.DATA

		numero_suministro = data["numero_suministro"]
		operario = request.user.operario
		consumo = data["consumo"]

		nuevo_consumo = Consumo()

		nuevo_consumo.operario = operario
		nuevo_consumo.consumo = consumo
		
		try:
			nuevo_consumo.cliente = Cliente.objects.get(numero_de_suministro=numero_suministro)
		except Cliente.DoesNotExist:
			return Response({'success':False,'reason':'No existe cliente con el número de suministro indicado.'},status=403)
		
		nuevo_consumo.save()
		serializer = ConsumoSerializer(nuevo_consumo)

		return Response(serializer.data)

#============================================================
# USER LOGIN
#============================================================
class UserLogin(APIView):

	permission_classes = (permissions.AllowAny,)

	def post(self, request, format=None):
		data  = request.DATA

		print request.DATA
		credentials = LoginSerializer(data=request.DATA)
		if credentials.is_valid():
			user = authenticate(username=credentials.object['username'], password=credentials.object['password'])
			
			if not user:
				return Response({'success':False,'reason':'bad credentials'},status=403)
			if not user.is_active:
				return Response({'success':False,'reason':'disabled account'},status=403)
				
			user = User.objects.get(id=user.id)
			token = Token.objects.get(user=user)

			print token.key

			operario = user.operario
			print "USER ============================"
			print user
			serializer = OperarioSerializer(operario)
			return Response({'success':True,'data': serializer.data,'token':token.key },status=200)
		else:
			return Response({'success':False,'reason':'bad credentials'},status=403)

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