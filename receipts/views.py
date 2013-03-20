from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin
from receipts.forms import ReceiptForm
from receipts.models import Receipt


class ReceiptActionMixin(object):

    def form_valid(self, form):
        msg = 'Receipt {0}!'.format(self.action)
        messages.info(self.request, msg)
        return super(ReceiptActionMixin, self).form_valid(form)

class ReceiptUserAccessMixin(object):
    """
    Tests if logged in User is allowed to see the called view
    """

    def dispatch(self, request, *args, **kwargs):
        receipt_user = Receipt.objects.get(id=self.kwargs["pk"]).user
        if request.user != receipt_user:
            raise PermissionDenied
        return super(ReceiptUserAccessMixin, self).dispatch(request,
                                                             *args, **kwargs)


class ReceiptDetailView(LoginRequiredMixin, ReceiptUserAccessMixin, DetailView):
    model = Receipt


class ReceiptListView(ListView):
    model = Receipt

    def get_context_data(self, **kwargs):
        context = super(ReceiptListView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        return context


class ReceiptCreateView(LoginRequiredMixin, ReceiptActionMixin, CreateView):

    form_class = ReceiptForm
    model = Receipt
    action = 'created'

    def form_valid(self, form):
        receipt = form.save(commit=False)
        receipt.user = self.request.user
        return super(ReceiptCreateView, self).form_valid(form)

    def get_initial(self):
        return {'user': self.request.user}


class ReceiptUpdateView(LoginRequiredMixin, ReceiptUserAccessMixin, ReceiptActionMixin, UpdateView):
    form_class = ReceiptForm
    model = Receipt
    action = 'updated'

class ReceiptDeleteView(LoginRequiredMixin, ReceiptActionMixin, DeleteView):
    model = Receipt
    action= 'deleted'
    success_url = reverse_lazy('receipts_index')
