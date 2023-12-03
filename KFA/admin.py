from django.contrib import admin
from .models import KFA, Review
# Register your models here.

@admin.register(KFA)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'option_price']

admin.site.register(Review)