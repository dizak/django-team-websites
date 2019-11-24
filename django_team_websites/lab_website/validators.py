"""
Custom validators for models and forms
"""
from django.core.exceptions import ValidationError
from . import models

def validate_unique_lab_name(name):
    """
    Raise ValidationError if a Lab entry with this name exists
    """
    lab = models.Lab.objects.filter(name=name)
    if lab.exists():
        raise ValidationError(
            f'{name} is already taken',
            params={'name': name},
        )

def validate_unique_lab_name_url(name_url):
    """
    Raise ValidationError if a Lab entry with this name_url exists
    """
    lab = models.Lab.objects.filter(name_url=name_url)
    if lab.exists():
        raise ValidationError(
            f'{name_url} is already taken',
            params={'name_url': name_url},
        )
