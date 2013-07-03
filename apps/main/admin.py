from django.contrib import admin
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django import forms

from apps.main.models import *


#==========================================
# 	CONSUMO ADMIN
#==========================================

class ConsumoAdmin(admin.ModelAdmin):
	list_display = ('cliente','fecha','consumo')

admin.site.register(Cliente)
admin.site.register(Operario)
admin.site.register(Consumo,ConsumoAdmin)
