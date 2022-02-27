"""Registry section paths."""
from django.urls import path

# This should contain paths related to registry ONLY
urlpatterns = [
    'cpovc_registry.views',
    path(r'^ou/$', 'home', name='registry'),
    path(r'^ou/new/$', 'register_new', name='registry_new'),
    path(r'^ou/view/(?P<org_id>\d+)/$', 'register_details', name='register_details'),
    path(r'^ou/edit/(?P<org_id>\d+)/$', 'register_edit', name='registry_edit'),
    path(r'^person/search/$', 'persons_search', name='search_persons'),
    path(r'^person/user/(?P<id>\d+)/$', 'new_user', name='new_user'),
    path(r'^person/$', 'person_actions', name='person_actions'),
    path(r'^person/new/$', 'new_person', name='new_person'),
    path(r'^person/edit/(?P<id>\d+)/$', 'edit_person', name='edit_person'),
    path(r'^person/view/(?P<id>\d+)/$', 'view_person', name='view_person'),
    path(r'^person/delete/(?P<id>\d+)/$', 'delete_person', name='delete_person'),
    path(r'^lookup/$', 'registry_look', name='reg_lookup'),
]
# {% path 'view_person' id=result.id %}
