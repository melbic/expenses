from django.contrib.auth.models import User
from django.forms import ModelForm
from receipts.models import Receipt
from django import forms
__author__ = 'dreiMac'


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        exclude = ('user',)
