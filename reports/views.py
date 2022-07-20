from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, FormView
from django.db.models import Q

from reports import forms
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.CompanyName
    paginate_by = 12
    paginate_orphans = 5
    template_name = "companys/company_list.html"
    context_object_name = "companys"


class ReportView(ListView):
    """ReportView Definition"""

    model = models.Report
    paginate_by = 12
    paginate_orphans = 5
    context_object_name = "reports"

    def get_context_data(self, **kwargs):
        context = super(ReportView, self).get_context_data(**kwargs)
        context["company_reports"] = models.Report.objects.filter(
            company_name__name=self.kwargs.get("company_pk")
        )
        return context


class DepartmentView(ListView):
    """ReportView Definition"""

    model = models.Report
    paginate_by = 12
    paginate_orphans = 5
    context_object_name = "department"
    template_name = "reports/departments/department_list.html"

    def get_context_data(self, **kwargs):
        context = super(DepartmentView, self).get_context_data(**kwargs)
        context["department_reports"] = models.Report.objects.filter(
            Q(company_name__name=self.kwargs.get("company_pk"))
            & Q(department__name=self.kwargs.get("department"))
        )
        return context


class ReportDetail(DetailView):
    """ReportDetail Definition"""

    model = models.Report
    context_object_name = "report"


class CreateReportView(FormView):
    """ReportCreate View"""

    form_class = forms.CreateReportForm
    template_name = "reports/report_create.html"

    def form_valid(self, form):
        report = form.save()
        report.save()
        form.save_m2m()
        return redirect(reverse("core:home"))
