from django.forms import ModelForm, ModelChoiceField, CharField, Textarea
from projects.models import ProjectParticipation
from receipts.models import Receipt

__author__ = 'dreiMac'


class ProjectModelChoiceField(ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.project


class ReceiptForm(ModelForm):

    def clean(self):
        cleaned_data = super(ModelForm, self).clean()
        receipt_date = cleaned_data.get("date")
        project = cleaned_data.get("project_participation").project

        if not (project.start_date <= receipt_date and (not project.end_date or receipt_date <= project.end_date) ):
            self._errors["date"] = self.error_class([u"The date should be during the project "])
            del cleaned_data["date"]
        return cleaned_data

    def __init__(self, *args, **kwargs):
        super(ReceiptForm, self).__init__(*args, **kwargs)
        self.fields['project_participation'] = ProjectModelChoiceField(queryset= ProjectParticipation.objects)

    description = CharField(widget=Textarea, label='Description')

    class Meta:
        model = Receipt