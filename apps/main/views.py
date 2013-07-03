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
	return render(request, "index.html")