from django.db import models
from django.utils.encoding import smart_text
from projects.models import ProjectParticipation


class Receipt(models.Model):
    """
    A receipt
    """
    number = models.PositiveIntegerField(editable=False)
    participation = models.ForeignKey(ProjectParticipation)
    title = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=255)
    amount_chf = models.DecimalField('Cost in CHF', max_digits=6, decimal_places=2)
    date = models.DateField()
    picture = models.ImageField(upload_to='Receipts/', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.number = self.participation.receipt_set.count()+1
        super(Receipt, self).save(args, kwargs)

    def number_of_receipts(self):
        """
        Returns the number of receipts in the same Participation as the specified.
        """
        return self.participation.receipt_set.count()

    def __unicode__(self):
        return smart_text(self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('receipts_detail', (), {"pk": self.pk})