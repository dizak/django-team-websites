# pylint: disable=import-outside-toplevel, no-member
# pylint: disable=attribute-defined-outside-init
"""
Unit- and functional tests
"""

from django.test import TestCase
from django.urls import reverse


class ViewsTests(TestCase):
    """
    Tests of views responses
    """
    fixtures = ["lab_test_data.json"]

    def setUp(self):
        """
        ViewsTests prerequisites set-up
        """
        from . import models
        self.models = models

        self.labs = self.models.Lab.objects.all()

    def test_index_view_lab_name(self):
        """
        Test if the index-view renders a response with the correct lab name
        """
        for i in self.labs:
            self.response = self.client.get(reverse(
                'lab:index-view',
                args=(i.name_url,),  # Mind this is a tuple
            ))
            self.assertContains(
                response=self.response,
                text=i.name,
                status_code=200,
            )

    def test_index_view_lab_about_us(self):
        """
        Test if the index-view renders response with correct
        """
        for i in self.labs:
            self.response = self.client.get(reverse(
                'lab:index-view',
                args=(i.name_url,),  # Mind this is a tuple
            ))
            self.assertContains(
                response=self.response,
                text=i.about_us,
                status_code=200,
                html=True,
            )
