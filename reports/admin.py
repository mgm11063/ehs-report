from django.contrib import admin
from django_admin_listfilter_dropdown.filters import (
    RelatedDropdownFilter,
)
from . import models


@admin.register(
    models.CompanyName,
    models.Department,
    models.Rater,
    models.Process,
    models.Place,
    models.RiskType,
    models.Factor,
    models.AfterPlan,
)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""

    list_display = ("name",)
    search_fields = ("name",)

    def __str__(self):
        return self.name


class ReportContentInline(admin.StackedInline):

    model = models.ReportContent
    extra = 0
    autocomplete_fields = ["risk_type", "factor"]
    filter_horizontal = ("after_plan",)


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):

    """Report Admin Definition"""

    inlines = (ReportContentInline,)

    fieldsets = (
        (
            "공통",
            {
                "fields": (
                    "company_name",
                    "department",
                    "rater",
                    "effective_date",
                    "process",
                    "place",
                )
            },
        ),
    )

    list_display = ("company_name", "department", "process")

    list_filter = (
        ("company_name", RelatedDropdownFilter),
        ("department", RelatedDropdownFilter),
        ("process", RelatedDropdownFilter),
    )

    autocomplete_fields = ["company_name", "department", "process", "place"]

    filter_horizontal = ("rater",)


@admin.register(models.ReportContent)
class ReportContentAdmin(admin.ModelAdmin):

    """Report Content Admin Definition"""

    pass
