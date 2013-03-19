from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.utils.encoding import smart_text


class Receipt(models.Model):
    """
    A receipt
    """
    user = models.ForeignKey(User)
    description = models.CharField(max_length=255)
    title = models.CharField(max_length=50, null=False)
    number = models.IntegerField()
    slug = models.SlugField()
    amount_chf = models.DecimalField('Cost in CHF', max_digits=6, decimal_places=2)

    def __unicode__(self):
        return smart_text(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('detail', (), {"slug": self.slug})

# class ReceiptForm(ModelForm):
#     class Meta:
#         model = Receipt