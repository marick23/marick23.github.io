from django.contrib import admin
from .models import KLEAGUE
# Register your models here.

@admin.register(KLEAGUE)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'option_price']