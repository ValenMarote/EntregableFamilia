from django.contrib import admin

# Register your models here.
from .models import familiar

class FamiliarAdmin(admin.ModelAdmin):
    list_display= ("Nombre", "Nacimiento", "Edad", "Trabajo")

admin.site.register(familiar, FamiliarAdmin)
