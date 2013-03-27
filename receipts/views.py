from django.core.urlresolvers import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from braces.views import LoginRequiredMixin
from receipts.forms import ReceiptForm
from receipts.models import Receipt, ProjectParticipation


class ReceiptActionMixin(object):

    def form_valid(self, form):
        msg = 'Receipt {0}!'.format(self.action)
        messages.info(self.request, msg)
        return super(ReceiptActionMixin, self).form_valid(form)


class UserFilterMixin(object):

    def get_queryset(self):
        # user=self.request.user
        return super(UserFilterMixin, self).get_queryset().filter(project_participation__user = self.request.user)


class ReceiptDetailView(LoginRequiredMixin, UserFilterMixin, DetailView):
    model = Receipt


class ReceiptListView(LoginRequiredMixin, UserFilterMixin, ListView):
    model = Receipt


class ReceiptCreateView(LoginRequiredMixin, UserFilterMixin, ReceiptActionMixin, CreateView):

    form_class = ReceiptForm
    model = Receipt
    action = 'created'

    def get_form(self, form_class):
        form = super(ReceiptCreateView, self).get_form(form_class)
        form.fields['project_participation'].queryset = ProjectParticipation.objects.filter(user=self.request.user)
        return form

    # def form_valid(self, form):
    #     receipt = form.save(commit=False)
    #     receipt.user = self.request.user
    #     return super(ReceiptCreateView, self).form_valid(form)
    #
    # def get_initial(self):
    #     return {'user': self.request.user}


class ReceiptUpdateView(LoginRequiredMixin, UserFilterMixin, ReceiptActionMixin, UpdateView):
    form_class = ReceiptForm
    model = Receipt
    action = 'updated'


class ReceiptDeleteView(LoginRequiredMixin, UserFilterMixin, ReceiptActionMixin, DeleteView):
    model = Receipt
    action = 'deleted'
    success_url = reverse_lazy('receipts_index')


