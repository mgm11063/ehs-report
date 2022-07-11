from django.urls import path
from reports import views as report_views

app_name = "core"


urlpatterns = [
    path("", report_views.HomeView.as_view(), name="home"),
]
