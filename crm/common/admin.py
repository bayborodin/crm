from django.contrib import admin
from .models import CommunicationType, Country, State


# CommunicationType model admin
class CommunicationTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "code", "is_phone"]
    list_filter = ["is_phone"]


admin.site.register(CommunicationType, CommunicationTypeAdmin)


# Country model admin
class CountryAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


admin.site.register(Country, CountryAdmin)


# State model admin
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


admin.site.register(State, StateAdmin)
