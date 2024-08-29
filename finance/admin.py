from django.contrib import admin
from .models import Ativo, Passivo, BalancoPatrimonial, DemonstracaoResultado


admin.site.register(Ativo)
admin.site.register(Passivo)
admin.site.register(BalancoPatrimonial)
admin.site.register(DemonstracaoResultado)