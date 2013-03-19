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
        regex=r'^(?P<slug>\w+)/$',
        view=ReceiptDetailView.as_view(),
        name='detail'
    ),
    url(
        regex=r'^(?P<pk>\w+)/update/$',
        view=ReceiptUpdateView.as_view(),
        name='update'
    ),
)