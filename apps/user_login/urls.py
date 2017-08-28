from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^all.json$', views.all_json),
    url(r'^all.html$', views.all_html),
    url(r'^find$', views.find),
    url(r'^create$', views.create),
    # url(r'^/(?P<id>\d+)$', views.show),
    # url(r'^/new$', views.new),
    # url(r'^/(?P<id>\d+)/edit$', views.edit),
    # url(r'^/update/(?P<id>\d+)$', views.update),
    # url(r'^/create$', views.create),
    # url(r'^/(?P<id>\d+)/delete$', views.delete)
]
