"""
Database models
"""
from django.db import models
from django.core.validators import validate_slug
from . import validators as custom_validators


class Lab(models.Model):
    """
    Lab model.
    """
    name = models.CharField(
        max_length=36,
        validators=[
            custom_validators.validate_unique_lab_name,
        ],
    )
    name_url = models.CharField(
        max_length=36,
        validators=[
            validate_slug,
            custom_validators.validate_unique_lab_name_url,
        ],
    )
    about_us = models.TextField(null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    """
    Person model
    """
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    name = models.CharField(max_length=36)
    position = models.CharField(max_length=36, null=True)
    room = models.CharField(max_length=5, null=True)

    def __str__(self):
        return self.name


class ResearchField(models.Model):
    """
    ReaseachField model
    """
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    people = models.ManyToManyField(Person)

    def __str__(self):
        return self.title


class Equipment(models.Model):
    """
    Equipment model
    """
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Publication(models.Model):
    """
    Publication model
    """
    authors = models.ManyToManyField(Person)

    title = models.CharField(max_length=300)
    journal = models.CharField(max_length=200)
    volume = models.PositiveSmallIntegerField()
    date = models.DateField()
    doi = models.CharField(max_length=100)

    def __str__(self):
        return self.title
