from django.contrib import admin
from . import models


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    """Custom Admin"""

    pass


@admin.register(models.Report)
class ReportAdmin(admin.ModelAdmin):
    """Custom User Admin"""

    pass


@admin.register(models.DepartmentType)
class DepartmentTypeAdmin(admin.ModelAdmin):
    """Custom Admin"""

    pass


@admin.register(models.ProcessType)
class ProcessTypeAdmin(admin.ModelAdmin):
    """Custom Admin"""

    pass
