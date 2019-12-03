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
        path(
            '<slug>/people/',
            view=views.PeopleView.as_view(),
            name='persons-view',
        ),
        path(
            '<slug>/publications/',
            view=views.PublicationsView.as_view(),
            name='publications-view',
        ),
        path(
            '<slug>/equipment/',
            view=views.EquipmentView.as_view(),
            name='equipment-view',
        ),
        path(
            '<slug>/research/',
            view=views.ResearchFieldView.as_view(),
            name='researchfield-view',
        )
]
