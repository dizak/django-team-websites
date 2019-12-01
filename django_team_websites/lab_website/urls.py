#pylint: disable=invalid-name

"""lab_website URL Configuration
"""
from django.urls import path
from . import views

urlpatterns = [
        path(
            '<slug>/',
            view=views.IndexView.as_view(),
            name='index-view',
        ),
]
