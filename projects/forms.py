from django import  forms
from django.forms import HiddenInput
from parsley.decorators import parsleyfy
from projects.models import Project, ProjectParticipation
from receipts.forms import ReceiptForm, ProjectModelChoiceField
from receipts.models import Receipt


@parsleyfy
class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        exclude=['slug']


class ParticipationForm(forms.ModelForm):
    class Meta:
        model=ProjectParticipation
        fields= ['user']


class ReceiptParticipationForm(ReceiptForm):
    participation = ProjectModelChoiceField(queryset= ProjectParticipation.objects,
                                            widget=HiddenInput)
