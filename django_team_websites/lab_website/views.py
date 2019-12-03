#pylint: disable=too-many-ancestors

"""
Views
"""

from django.views.generic.detail import DetailView
from . import models

class IndexView(DetailView):
    """
    Index view and a parent view for the other views.
    Based on django.views.generic.detail.DetailView
    """
    model = models.Lab
    slug_field = 'name_url'


class ResearchFieldView(IndexView):
    """
    View for Research Field page.
    Based on .views.IndexView
    """
    template_name = 'lab_website/research.html'

    def get_context_data(self, **kwargs):
        """
        Context containing research field
        """
        context = super().get_context_data(**kwargs)
        context['research'] = models.ResearchField.objects.filter(#pylint: disable=no-member
            lab__name_url=context['object'].name_url,
        )
        return context


class PeopleView(IndexView):
    """
    View for people page.
    Based on .views.IndexView
    """
    template_name = 'lab_website/people.html'

    def get_context_data(self, **kwargs):
        """
        Context containing Persons
        """
        context = super().get_context_data(**kwargs)
        context['people'] = models.Person.objects.filter(#pylint: disable=no-member
            lab__name_url=context['object'].name_url,
        )
        return context


class PublicationsView(PeopleView):
    """
    View for publications page.
    Based on .views.IndexView
    """
    template_name = 'lab_website/publications.html'

    def get_context_data(self, **kwargs):
        """
        Context containing Publications and Persons
        """
        context = super().get_context_data(**kwargs)
        persons_names = [i.name for i in context['people']]
        context['publications'] = models.Publication.objects.filter(#pylint: disable=no-member
            authors__name__in=persons_names,
        )
        return context


class EquipmentView(IndexView):
    """
    View for equipment page.
    Based on .views.IndexView
    """
    template_name = 'lab_website/equipment.html'

    def get_context_data(self, **kwargs):
        """
        Context containing Equipment
        """
        context = super().get_context_data(**kwargs)
        context['equipment'] = models.Equipment.objects.filter(#pylint: disable=no-member
            lab__name_url=context['object'].name_url,
        )
        return context
