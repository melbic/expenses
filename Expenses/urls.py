from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.views.generic import RedirectView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Expenses.views.home', name='home'),
    # url(r'^Expenses/', include('Expenses.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(
        regex=r'^$',
         view='Expenses.views.view_expenses',
         name='home'
     ),
     url(r'^admin/',
         include(admin.site.urls)
     ),
     url(
         r'^login/$',
         'django.contrib.auth.views.login',
         {'template_name': 'login.html'},
         name="login",

     ),
     url(
         r'^logout',
         'Expenses.views.logout_view',
         name="logout"
     ),
     url(r'^receipts/',
         include('receipts.urls'),
         name='receipts'
     ),
     url(r'^projects/',
         include('projects.urls'),
         name='projects'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                                }),
                            )