from django.contrib import admin

from .models import Requerimento
from .models import Anexo
from .models import Despacho
from .models import TipoRequerimento
from .models import Curso

admin.site.register(Requerimento)
admin.site.register(Anexo)
admin.site.register(Despacho)
admin.site.register(Curso)
admin.site.register(TipoRequerimento)