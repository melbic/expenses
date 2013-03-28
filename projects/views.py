# Create your views here.
from braces.views import StaffuserRequiredMixin
from django.contrib.auth.decorators import user_passes_test, login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView
from projects.forms import ProjectForm, ParticipationForm, ReceiptParticipationForm
from projects.models import ProjectParticipation, Project
from receipts.forms import ReceiptForm
from receipts.models import Receipt


@user_passes_test(lambda u: u.is_staff)
def add_project(request):
    form=ProjectForm(request.POST or None)
    if form.is_valid():
        project=form.save(commit=False)
        project.save()
        return redirect(project)
    return render_to_response('projects/project_form.html', {'form': form}, context_instance=RequestContext(request))


@user_passes_test(lambda u: u.is_staff)
def view_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    form = ParticipationForm(request.POST or None)
    participations = ProjectParticipation.objects.filter(project=project)
    receipts = Receipt.objects.filter(participation__in=participations)
    users = participations.values_list('user', flat=True).order_by('user')
    form.fields['user'].queryset = form.fields['user'].queryset.exclude(id__in=users)
    if form.is_valid():
        participation = form.save(commit=False)
        participation.project = project
        participation.save()
        return redirect(request.path)
    return render_to_response('projects/project_detail.html', { 'project': project, 'form': form},
                       context_instance=RequestContext(request))

@user_passes_test(lambda u: u.is_staff)
def participation_remove(request, slug, pk):
    if request.POST:
        ProjectParticipation.objects.get(id=pk).delete()
        return HttpResponse(status=200)
    return HttpResponse(status=404)


class ProjectListView(StaffuserRequiredMixin, ListView):
    model = Project


@login_required
def participation_detail(request, pk):
    participation = get_object_or_404(ProjectParticipation, id=pk)
    receipts = Receipt.objects.filter(participation=participation)
    form = ReceiptParticipationForm(request.POST or None,initial={'participation': participation})

    if form.is_valid():
        receipt = form.save(commit=False)
        receipt.participation = participation
        receipt.save()
        return redirect(request.path)
    return render_to_response('projects/participation_detail.html', {'participation' : participation,
                                                                     'receipts' : receipts,
                                                                     'form' : form},
                              context_instance=RequestContext(request))