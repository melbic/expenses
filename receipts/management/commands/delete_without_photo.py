from django.core.management.base import NoArgsCommand
from receipts.models import Receipt

__author__ = 'dreiMac'

class Command(NoArgsCommand):
    help= """
            deletes all receipts without photos
          """

    def handle_noargs(self, **options):
        illegal_receipts = Receipt.objects.filter(has_picture=True)
        illegal_receipts.delete()