from django.conf.urls import url

from .views import (
    post_list,
    post_create,
    post_delete,
    post_detail,
    post_update
)


urlpatterns = [
  
    url(r'^$', post_list,name='list'),
    url(r'^create/$', post_create),
    url(r'^(?P<id>\d+)/update/$', post_update,name='update'),
    url(r'^(?P<id>\d+)/delete/$', post_delete),
    url(r'^(?P<id>\d+)/$', post_detail, name='detail'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]