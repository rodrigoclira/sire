from django.contrib import admin

from .models import Requerimento
from .models import Anexo
from .models import Despacho

admin.site.register(Requerimento)
admin.site.register(Anexo)
admin.site.register(Despacho)