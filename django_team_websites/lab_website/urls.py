#pylint: disable=invalid-name

"""lab_website URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
        path('<slug:name_url>/', view=views.index)
]
