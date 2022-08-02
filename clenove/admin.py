from django.contrib import admin

# Register your models here.

from .models import Skaut

class SkautAdmin(admin.ModelAdmin):
    list_display = ["jmeno", "prezdivka", "vek", "slozil_zkousku"]
    list_filter = ["vek", "slozil_zkousku"]

admin.site.register(Skaut, SkautAdmin)

