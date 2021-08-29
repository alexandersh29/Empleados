from django.contrib import admin
from .models import Empleados


# Register your models here.

class AdministrarModelo(admin.ModelAdmin):
    list_display = ('id','nombre','apellido','area', 'cargo')
    search_fields = ('id','nombre','apellido','area', 'cargo')
    date_hierarchy = 'created'
    list_filter = ('nombre', 'area')

admin.site.register(Empleados, AdministrarModelo)


