from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("<str:company_pk>", views.ReportView.as_view(), name="list"),
    path(
        "<str:company_pk>/<str:department>/",
        views.DepartmentView.as_view(),
        name="department",
    ),
    path(
        "<str:company_pk>/<str:department>/<int:pk>",
        views.ReportDetail.as_view(),
        name="detail",
    ),
    path("<str:company_pk>/create", views.CreateReportView.as_view(), name="create"),
]
