from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.encoding import smart_text


class Receipt(models.Model):
    """
    A receipt
    """
    number = models.PositiveIntegerField(editable=False)
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255)
    amount_chf = models.DecimalField('Cost in CHF', max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        self.number = self.user.receipt_set.count()+1
        super(Receipt, self).save(args, kwargs)

    def number_of_receipts(self):
        return self.user.receipt_set.count()

    def __unicode__(self):
        return smart_text(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {"pk": self.pk})