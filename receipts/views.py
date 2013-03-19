from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib import messages

from receipts.models import Receipt

class ReceiptActionMixin(object):

    def form_valid(self, form):
        msg = 'Receipt {0}!'.format(self.action)
        messages.info(self.request, msg)
        return super(ReceiptActionMixin, self).form_valid(form)

class ReceiptDetailView(DetailView):
    model = Receipt

# class ReceiptResultsView(ReceiptDetailView):
#     template_name = 'receipts/results.html'

class ReceiptListView(ListView):
    model = Receipt

class ReceiptCreateView(ReceiptActionMixin, CreateView):
    model = Receipt
    action = 'created'

class ReceiptUpdateView(ReceiptActionMixin, UpdateView):
    model = Receipt
    action = 'updated'