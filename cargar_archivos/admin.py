from django.contrib import admin
from .models import update_archivo, products

class update_archivos_admin(admin.ModelAdmin):
    list_display = ["archivo"]
    list_filter = ["archivo"]

admin.site.register(products)
admin.site.register(update_archivo, update_archivos_admin)