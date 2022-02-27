"""paths for reports."""
from django.urls import path

# This should contain paths related to report ONLY
urlpatterns = [
    'cpovc_reports.views',
    path(r'^$', 'reports_home', name='reports'),
    path(r'^documents/$', 'reports_home', name='document_reports'),
    path(r'^(?P<id>\d+)/$', 'reports_cpims', name='cpims_reports'),
    path(r'^caseload/$', 'reports_caseload', name='caseload_reports'),
    path(r'^get_viral_load_report/$', 'get_viral_load_report', name='get_viral_load_report'),
    path(r'^manage/$', 'manage_reports', name='manage_reports'),
    path(r'^dashboard/$', 'manage_dashboard', name='manage_dashboard'),
    path(r'^download/(?P<file_name>[0-9A-Za-z_\.=\-\' ]+)$', 'reports_download', name='download_reports'),
    path(r'^generate/$', 'reports_generate', name='generate_reports'),
    path(r'^pivot/$', 'reports_pivot', name='pivot_reports'),
    path(r'^data/$', 'reports_rawdata', name='pivot_rawdata'),
    path(r'^datim/$', 'reports_ovc_pivot', name='pivot_ovc_reports'),
    path(r'^datim_mer/$', 'reports_ovc_datim_mer_pivot', name='pivot_ovc_reports_mer'),
    path(r'^datim_mer23/$', 'reports_ovc_datim_mer23_pivot', name='pivot_ovc_reports_mer23'),
    path(r'^datim_mer24/$', 'reports_ovc_datim_mer24_pivot', name='pivot_ovc_reports_mer24'),
    path(r'^datim_mer25/$', 'reports_ovc_datim_mer25_pivot', name='pivot_ovc_reports_mer25'),
    path(r'^pepfar/$', 'reports_ovc_pepfar', name='pivot_ovc_pepfar'),
    path(r'^kpi/$', 'reports_ovc_kpi', name='pivot_ovc_kpi'),
    path(r'^viral_load/$', 'viral_load', name='viral_load'),
    path(r'^ovcdata/$', 'reports_ovc_rawdata', name='pivot_ovc_rawdata'),
    path(r'^download/$', 'reports_ovc_download', name='ovc_download'),
    path(r'^ovc/(?P<id>\d+)/$', 'reports_ovc', name='reports_ovc'),
    path(r'^dashboard/data/$', 'dashboard_details', name='dashboard_details'),
    path(r'^cluster/$', 'cluster', name='cluster'),
    path(r'^ovc/$', 'reports_ovc_list', name='reports_ovc_list'),
     path(r'^bursary/$', 'reports_bursary', name='bursary_reports'),
    ]


