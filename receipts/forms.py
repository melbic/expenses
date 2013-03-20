from django.forms import ModelForm
from receipts.models import Receipt
__author__ = 'dreiMac'


class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        exclude = ('user',)
