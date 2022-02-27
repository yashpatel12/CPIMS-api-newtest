"""cpims URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""
cpims URL Configuration.
Other urls are import
Put here only urls not specific to app
"""
import logging

from django.urls import (include, path)
from django.contrib import admin
from cpovc_auth import urls as auth_urls
from cpovc_registry import urls as registry_urls
from cpovc_forms import urls as forms_urls
from cpovc_reports import urls as reports_urls
from cpovc_gis import urls as gis_urls
from cpovc_api import urls as api_urls
from cpovc_ovc import urls as ovc_urls
from cpovc_settings import urls as settings_urls
from data_cleanup import urls as data_cleanup_urls
from cpovc_offline_mode import urls as offline_mode_urls
from django.contrib.auth.urls import (password_reset, password_change, password_change_done)
from cpovc_auth.views import password_reset
from django.views.generic import TemplateView
from cpovc_dashboard import urls as dashboard_api_urls
from cpovc_access.forms import StrictPasswordChangeForm

urlpatterns = [
    path(r'^admin/', include(admin.site.urls), name='admin'),
    # url(r'^$', 'cpovc_auth.views.log_in', name='home'),
    path(r'^public_dashboard/registration/', 'cpims.views.public_dashboard_reg', name='public_dashboard_reg'),
    path(r'^public_dashboard/hivstat/', 'cpims.views.public_dashboard_hivstat', name='public_dashboard_hivstat'),
    path(r'^public_dashboard/served/', 'cpims.views.public_dashboard_served', name='public_dashboard_served'),
    path(r'^public_dash/', 'cpims.views.public_dash', name='public_dash'),
    path(r'^public_dashboard/', 'cpims.views.public_dashboard_reg', name='public_dashboard_reg'),
    # APIs
    path(r'^get_locality_data/', 'cpims.views.get_locality_data', name='get_locality_data'),
    path(r'^hiv_stats_pub_data/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_pub_data', name='get_pub_data'),
    path(r'^hiv_stats_ovc_active/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_ovc_active_hiv_status',
         name='ovc_active_hiv_status'),
    path(r'^get_hiv_suppression_data/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_hiv_suppression_data',
         name='get_hiv_suppression_data'),
    # ####
    path(r'^get_total_ovc_ever/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_total_ovc_ever',
         name='get_total_ovc_ever'),
    path(r'^get_total_ovc_ever_exited/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_total_ovc_ever_exited',
         name='get_total_ovc_ever_exited'),
    path(r'^get_total_wout_bcert_at_enrol/(?P<org_level>\w+)/(?P<area_id>.*)/',
         'cpims.views.get_total_wout_bcert_at_enrol', name='get_total_wout_bcert_at_enrol'),
    path(r'^get_total_w_bcert_2date/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_total_w_bcert_2date',
         name='get_total_w_bcert_2date'),
    path(r'^get_total_s_bcert_aft_enrol/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_total_s_bcert_aft_enrol',
         name='get_total_s_bcert_aft_enrol'),
    path(r'^fetch_cbo_list/', 'cpims.views.fetch_cbo_list', name='fetch_cbo_list'),
    path(r'^get_ever_tested_hiv/(?P<org_level>\w+)/(?P<area_id>.*)/', 'cpims.views.get_ever_tested_hiv',
         name='get_ever_tested_hiv'),

    path(
        r'^get_new_ovcregs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/',
        'cpims.views.get_new_ovcregs_by_period', name='get_new_ovcregs_by_period'),

    path(
        r'^get_active_ovcs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/',
        'cpims.views.get_active_ovcs_by_period', name='get_active_ovcs_by_period'),

    path(
        r'^get_exited_ovcs_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/',
        'cpims.views.get_exited_ovcs_by_period', name='get_exited_ovcs_by_period'),

    path(
        r'^get_exited_hsehlds_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/',
        'cpims.views.get_exited_hsehlds_by_period', name='get_exited_hsehlds_by_period'),

    path(r'^get_served_bcert_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<month_year>.*)/',
         'cpims.views.get_served_bcert_by_period', name='get_served_bcert_by_period'),
    path(r'^get_u5_served_bcert_by_period/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<month_year>.*)/',
         'cpims.views.get_u5_served_bcert_by_period', name='get_u5_served_bcert_by_period'),
    path(
        r'^get_ovc_served_stats/(?P<org_level>\w+)/(?P<area_id>.*)/(?P<funding_partner>.*)/(?P<funding_part_id>.*)/(?P<period_type>.*)/',
        'cpims.views.get_ovc_served_stats', name='get_ovc_served_stats'),
    # endAPIs
    path(r'^$', 'cpims.views.home', name='home'),
    # url(r'^home/$', 'cpims.views.home', name='home'),
    path(r'^accounts/request/$', 'cpims.views.access', name='access'),
    path(r'^accounts/terms/(?P<id>\d+)/$', 'cpovc_access.views.terms',
         name='terms'),
    path(r'^login/$', 'cpovc_auth.views.log_in', name='login'),
    path(r'^logout/$', 'cpovc_auth.views.log_out', name='logout'),
    path(r'^register/$', 'cpovc_auth.views.register', name='register'),
    path(r'^auth/', include(auth_urls)),
    path(r'^registry/', include(registry_urls)),
    path(r'^forms/', include(forms_urls)),
    path(r'^reports/', include(reports_urls)),
    path(r'^gis/', include(gis_urls)),
    path(r'^api/', include(api_urls)),
    path(r'^ovcare/', include(ovc_urls)),
    path(r'^settings/', include(settings_urls)),
    path(r'^data_cleanup/', include(data_cleanup_urls)),
    path(r'^accounts/login/$', 'cpovc_auth.views.log_in', name='login'),
    path(r'^accounts/password/reset/$', password_reset,
         {'template_name': 'registration/password_reset.html'},
         name='password_reset'),
    path(r'^accounts/password/reset/done/$', password_reset,
         {'template_name': 'registration/password_reset_done.html'},
         name='password_reset_done'),
    path(r'^accounts/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
         'cpovc_auth.views.reset_confirm', name='password_reset_confirm'),
    path(r'^reset/$', 'cpovc_auth.views.reset', name='reset'),
    path(r'^accounts/password/change/$', password_change,
         {'post_change_redirect': '/accounts/password/change/done/',
          'template_name': 'registration/password_change.html',
          'password_change_form': StrictPasswordChangeForm},
         name='password_change'),
    path(r'^accounts/password/change/done/$', password_change_done,
         {'template_name': 'registration/password_change_done.html'}),
    path(r'^F57665A859FE7CFCDB6C8935196374AD\.txt$',
         TemplateView.as_view(template_name='comodo.txt',
                              content_type='text/plain')),
    path(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt',
                                                content_type='text/plain')),

    path(r'^offline_mode/', include(offline_mode_urls)),
    # url(r'^dashboard/$', 'cpovc_dashboard.views.ovc_dashboard', name='ovc_dashboard'),
    path(r'^d/$', 'cpovc_dashboard.views.ovc_dashboard', name='ovc_dashboard'),
    path(r'^d/hivstat/', 'cpovc_dashboard.views.ovc_dashboard_hivstat', name='hivstat_dash'),
    path(r'^d/services/', 'cpovc_dashboard.views.ovc_dashboard_services', name='services_dash'),
    path(r'^d/cm/', 'cpovc_dashboard.views.ovc_dashboard_cm', name='cm_dash'),
    path(r'^api/v2/', include(dashboard_api_urls)),
]

handler400 = 'cpims.views.handler_400'
handler404 = 'cpims.views.handler_404'
handler500 = 'cpims.views.handler_500'

admin.site.site_header = 'CPIMS Administration'
admin.site.site_title = 'CPIMS administration'
admin.site.index_title = 'CPIMS admin'
