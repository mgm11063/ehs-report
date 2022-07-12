from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Company
    paginate_by = 12
    paginate_orphans = 5
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
            company__name=self.kwargs.get("company_pk")
        )
        return context


class ReportDetail(DetailView):
    """ReportDetail Definition"""

    model = models.Report
    context_object_name = "report"
