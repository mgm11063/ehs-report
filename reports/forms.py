from django import forms
from django.forms import TextInput
from . import models


class CreateReportForm(forms.ModelForm):
    class Meta:
        model = models.Report
        fields = (
            "company",
            "department",
            "process",
            "operation",
            "effective_date",
            "prev_image",
            "prev_risk",
            "prev_frequency",
            "prev_importance",
            "after_image",
            "after_risk",
            "after_frequency",
            "after_importance",
            "improvement_date",
            "improvement_officer",
            "is_completion",
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
