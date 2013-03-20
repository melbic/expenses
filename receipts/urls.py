from django.conf.urls import patterns, url
from .views import ReceiptDetailView, ReceiptListView, ReceiptCreateView, ReceiptUpdateView, ReceiptDeleteView

urlpatterns = patterns('',
    url(r'^$',
       view=ReceiptListView.as_view(),
       name='receipts_index'
    ),
    url(
        regex=r'^create/$',
        view=ReceiptCreateView.as_view(),
        name='receipts_create'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=ReceiptDetailView.as_view(),
        name='receipts_detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=ReceiptUpdateView.as_view(),
        name='receipts_update'
    ),
    url(
        regex=r'^(?P<pk>\d+)/delete/$',
        view=ReceiptDeleteView.as_view(),
        name='receipts_delete'
    ),
)