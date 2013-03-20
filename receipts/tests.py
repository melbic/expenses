"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.contrib.auth.models import User

from django.test import TestCase
from receipts.models import Receipt


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class FormTest(TestCase):

    def setUp(self):
        self.user = User()
        self.user.save()

    def create_receipt(self):
        receipt = Receipt(user=self.user)
        receipt.description = u"Test"
        receipt.title = u"Title"
        receipt.amount_chf = 10
        receipt.save()
        return receipt

    def test_form(self):
        receipt1 = self.create_receipt()
        self.assertEquals(1, receipt1.number)
        receipt2 = self.create_receipt()
        self.assertEquals(2, receipt2.number)

