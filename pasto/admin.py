"""Admin displays for Pasto"""
from django.contrib import admin
from .models import Code

admin.site.register(Code, admin.ModelAdmin)
