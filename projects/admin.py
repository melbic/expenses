from .models import Project, ProjectParticipation
from django.contrib import admin


class ProjectParticipationInline(admin.TabularInline):
    model = ProjectParticipation



class ProjectAdmin(admin.ModelAdmin):
    inlines =  [ProjectParticipationInline]
    list_display = ('__str__', 'start_date', 'end_date',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectParticipation)
