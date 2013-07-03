#!--coding:utf-8--#

from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.core.mail import send_mail
from django.forms.models import model_to_dict
from django.contrib import messages
from pprint import pprint
from datetime import datetime

from apps.main.models import *

from django.views.decorators.csrf import ensure_csrf_cookie

#---------------------------------------------------------------
#	INDEX
#---------------------------------------------------------------

@ensure_csrf_cookie
def home(request):
	if request.user.is_authenticated():
		clientes = Cliente.objects.all()
		return render(request,"main/index.html",{'clientes':clientes})
	else:
		return render(request,"index.html")

#---------------------------------------------------------------
#	LOGOUT
#---------------------------------------------------------------

from django.contrib.auth import authenticate
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

def logout(request):
	auth_logout(request)
	request.session.clear()
	return HttpResponseRedirect("/")

def clientes(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	clientes  = Cliente.objects.all()
	return render(request, "main/clientes.html",{'clientes':clientes})

def consumos(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	consumos  = Consumo.objects.all()
	return render(request, "main/consumos.html",{'consumos':consumos})

def cliente(request,pk=None):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	cliente = Cliente.objects.get(id=pk)
	return render(request, "main/cliente.html",{'cliente':cliente})

def operarios(request):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	operarios = Operario.objects.all()
	return render(request, "main/operarios.html",{'operarios':operarios})

def operario(request,pk=None):
	if not request.user.is_authenticated():
		return HttpResponseRedirect("/")

	operario = Operario.objects.get(id=pk)
	return render(request, "main/operario.html",{'operario':operario})
