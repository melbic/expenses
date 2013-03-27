"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from projects.management.commands.insert_sample_data import create_project


class ProjectTest(TestCase):

    def testCreation(self):
        project = create_project(1)
        self.assertTrue(project.name == "Test1")
        self.assertTrue(project.start_date == "2011-1-1")