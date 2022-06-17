from django.contrib import admin
from .models import Familia

class FamiliaAdmin(admin.ModelAdmin):
    list_display = ('edad','parentezco','fecha_cumpleanios')

admin.site.register(Familia,FamiliaAdmin)