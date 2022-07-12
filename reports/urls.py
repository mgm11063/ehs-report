from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    path("<str:company_pk>", views.ReportView.as_view(), name="list"),
    path("<str:company_pk>/<int:pk>", views.ReportDetail.as_view(), name="detail"),
]
