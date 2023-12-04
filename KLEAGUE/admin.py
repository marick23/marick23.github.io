from django.contrib import admin
from .models import KLEAGUE, Category
# Register your models here.

@admin.register(KLEAGUE)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'base_price', 'option_price']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)