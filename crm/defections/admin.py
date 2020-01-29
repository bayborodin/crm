from django.contrib import admin

from .models import Defection, Photo


class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 0


class DefectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'created', 'updated', 'account', 'shipment', 'offering', 'kind']
    inlines = [PhotoInline]


admin.site.register(Defection, DefectionAdmin)
