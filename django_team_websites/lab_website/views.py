#pylint: disable=too-many-ancestors

"""
Views
"""

from django.views.generic.detail import DetailView
from . import models

class IndexView(DetailView):
    """
    View for index page. Based on django.views.generic.detail.DetailView
    """
    template_name = 'lab_website/index.jj2.html'
    model = models.Lab
    slug_field = 'name_url'
