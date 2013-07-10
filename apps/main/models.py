# -*- coding: ISO-8859-1 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import (
	BaseUserManager,AbstractUser, AbstractBaseUser, UserManager
)

from django.contrib.auth.hashers import (
	check_password, make_password, is_password_usable, UNUSABLE_PASSWORD
)

from django.contrib.auth.models import User

from datetime import date
from datetime import datetime

from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save

#------------------------------------------------------------------------
#	Cliente
#------------------------------------------------------------------------

class Cliente(models.Model):

	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	numero_de_suministro = models.IntegerField()

	def __unicode__(self):
		return self.nombres + " " + self.apellidos

	class Meta:
		db_table = "Cliente"
		verbose_name = "cliente"
		verbose_name_plural = "clientes"


#------------------------------------------------------------------------
#	Operario
#------------------------------------------------------------------------

class Operario(models.Model):

	user = models.OneToOneField(User)
	nombres = models.CharField(max_length=255)
	apellidos = models.CharField(max_length=255)
	codigo = models.IntegerField()

	def __unicode__(self):
		return self.nombres + " " + self.apellidos
		
	class Meta:
		db_table = "Operario"
		verbose_name = "operario"
		verbose_name_plural = "operarios"


#------------------------------------------------------------------------
#	Consumo
#------------------------------------------------------------------------

class Consumo(models.Model):

	consumo = models.DecimalField(_("consumption"),decimal_places=6,max_digits=12,blank=False)
	cliente = models.ForeignKey(Cliente,verbose_name=_('client'))
	operario = models.ForeignKey(Operario,verbose_name=_('operario'))
 	fecha = models.DateField(auto_now = True)

 	def __unicode__(self):
 		return "Registro de consumo del cliente " + self.cliente.nombres

 	class Meta:
 		db_table = "Consumo"
 		verbose_name = "consumo"
 		verbose_name_plural = "consumos"


@receiver(post_save, sender=User)
def create_auth_token_baseuser(sender, instance=None, created=False, **kwargs):
	if created:
		Token.objects.create(user=instance)




