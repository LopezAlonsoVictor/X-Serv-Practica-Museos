from django.contrib import admin

# Register your models here.

from .models import Usuario
from .models import Comentario
from .models import Seleccion
from .models import Museo

admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Seleccion)
admin.site.register(Museo)
