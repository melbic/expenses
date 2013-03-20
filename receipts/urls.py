from django.conf.urls import patterns, url
from .views import ReceiptDetailView, ReceiptListView, ReceiptCreateView, ReceiptUpdateView

urlpatterns = patterns('',
    url(r'^$',
       view=ReceiptListView.as_view(),
       name='index'
    ),
    url(
        regex=r'^create/$',
        view=ReceiptCreateView.as_view(),
        name='create'
    ),
    url(
        regex=r'^(?P<pk>\d+)/$',
        view=ReceiptDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\d+)/update/$',
        view=ReceiptUpdateView.as_view(),
        name='update'
    ),
)