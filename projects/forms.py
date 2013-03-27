from django import  forms
from parsley.decorators import parsleyfy
from projects.models import Project, ProjectParticipation

@parsleyfy
class ProjectForm(forms.ModelForm):

    class Meta:
        model=Project
        exclude=['slug']


class ParticipationForm(forms.ModelForm):
    class Meta:
        model=ProjectParticipation
        fields= ['user']