from django.contrib import admin
from .models import Ativo, Passivo, BalancoPatrimonial


admin.site.register(Ativo)
admin.site.register(Passivo)
admin.site.register(BalancoPatrimonial)