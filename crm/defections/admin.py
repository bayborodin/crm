from django.contrib import admin

from .models import Defection


class DefectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'updated', 'account']


admin.site.register(Defection, DefectionAdmin)
