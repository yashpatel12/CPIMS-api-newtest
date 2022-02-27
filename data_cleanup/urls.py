"""Data cleanup section paths."""
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import DataQualityView, CasePlanDataQualityView

urlpatterns = [
    'data_cleanup.views',
    path(r'^filter/$', login_required(
        DataQualityView.as_view()), name='data_cleanup'),
    path(r'^filter/case_plan$', login_required(
        CasePlanDataQualityView.as_view()), name='data_cleanup_case_plan')
]
