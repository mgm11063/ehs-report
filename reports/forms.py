from django import forms
from django.forms import TextInput
from . import models


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = (
            "company_name",
            "department",
            "rater",
            "effective_date",
            "process",
            "place",
        )
        widgets = {
            "operation": TextInput(attrs={"placeholder": "작업내용"}),
        }

    def save(self, *args, **kwargs):
        report = super().save(commit=False)
        return report

        # "department": ModelChoiceField(
        #     queryset=models.DepartmentType.objects.all()
        # ),
