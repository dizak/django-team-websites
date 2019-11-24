"""
Views
"""

from django.shortcuts import render
from . import models

# Create your views here.

def index(
    request,
    name_url:str,
):
    """
    Index page view
    """
    lab = models.Lab(name_url=name_url)
    return render(
        request,
        'lab_website/base.jj2.html',
        {
            'lab_name': lab.name_url,
        }
    )
