"""
Models registered in the admin panel
"""
from django.contrib import admin
from . import models

admin.site.register(models.Lab)
admin.site.register(models.Person)
admin.site.register(models.ResearchField)
admin.site.register(models.Publication)
