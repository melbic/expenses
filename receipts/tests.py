"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime
from django.contrib.auth.models import User

from django.test import TestCase
import receipts
from receipts.forms import ReceiptForm
from receipts.models import Receipt, Project, ProjectParticipation


class FormTest(TestCase):

    def setUp(self):
        self.user = User()
        self.user.save()
        self.project = Project()
        self.project.start_date= datetime.date(2012,1,1)
        self.project.end_date=datetime.date(2012,12,31)
        self.project.save()

        self.project_participation = ProjectParticipation()
        self.project_participation.project=self.project
        self.project_participation.user = self.user
        self.project_participation.save()

    def create_receipt(self):
        receipt = Receipt()
        receipt.description = u"Test"
        receipt.title = u"Title"
        receipt.amount_chf = 10
        receipt.date = datetime.date(2012,8,2)
        receipt.participation = self.project_participation
        receipt.save()
        return receipt

    def test_form(self):
        receipt1 = self.create_receipt()
        self.assertEquals(1, receipt1.number)
        receipt2 = self.create_receipt()
        self.assertEquals(2, receipt2.number)

    def test_form_date(self):
        receipt = self.create_receipt()
        receipt.date=datetime.date.today()
        form = ReceiptForm(instance=receipt)
        self.assertFalse(form.is_valid())

        receipt2 = self.create_receipt()
        form2 = ReceiptForm(instance=receipt2)
        self.assertTrue(form2.is_valid())