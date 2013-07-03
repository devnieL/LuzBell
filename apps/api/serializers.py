from apps.main.models import *

from rest_framework import serializers
from pprint import pprint

from rest_framework.serializers import (
	HyperlinkedModelSerializerOptions,
	HyperlinkedModelSerializer
)

#=============================================================
#	Consumo Serializer
#=============================================================

class ConsumoSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.Field()
	class Meta:
		model = Consumo

#=============================================================
#	Operario Serializer
#=============================================================

class OperarioSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.Field()
	class Meta:
		model = Operario

#=============================================================
#	Cliente Serializer
#=============================================================

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.Field()
	class Meta:
		model = Cliente
