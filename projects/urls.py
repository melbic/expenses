from django.conf.urls import patterns, url
from projects.views import ProjectListView

urlpatterns = patterns('',
                       url(r'^$',
                           view=ProjectListView.as_view(),
                           name='project_index'
                       ),
                       url(
                           regex=r'^create/$',
                           view='projects.views.add_project',
                           name='project_create'
                       ),
                       url(
                           regex=r'^(?P<slug>[-\w]+)$',
                           view='projects.views.view_project',
                           name='projects_detail'
                           ),
                        url(
                            regex=r'^(?P<slug>[-\w]+)/(?P<pk>\d+)/delete/$',
                            view='projects.views.participation_remove',
                            name='participation_remove'
                        ),
)