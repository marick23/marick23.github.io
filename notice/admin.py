from django.contrib import admin
from .models import Notice
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(Notice, MarkdownxModelAdmin)

# Register your models here.
