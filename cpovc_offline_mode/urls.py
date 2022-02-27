from django.urls import path

urlpatterns = [
    'cpovc_offline_mode.views',
    path(r'^templates/$', 'templates', name='templates'),
    path(r'^data/$', 'fetch_data', name='fetch_data'),
    path(r'^services/$', 'fetch_services', name='fetch_services'),
    path(r'^submit/$', 'submit_form', name='submit_form'),
]

