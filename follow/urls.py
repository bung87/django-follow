try:
    from django.conf.urls import url, include
except ImportError:
    from django.conf.urls.defaults import *
from . import views
urlpatterns = (
    url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', views.toggle, name='toggle'),
    url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', views.toggle, name='follow'),
    url(r'^toggle/(?P<app>[^\/]+)/(?P<model>[^\/]+)/(?P<id>\d+)/$', views.toggle, name='unfollow'),
    url(r'^vendorfollowers/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', views.get_vendor_followers, name='get_vendor_followers'),
	url(r'^vendorfollowing/(?P<content_type_id>\d+)/(?P<object_id>\d+)/$', views.get_vendor_following, name='get_vendor_following'),
    url(r'^vendor_followers_subset/(?P<content_type_id>\d+)/(?P<object_id>\d+)/(?P<sIndex>\d+)/(?P<lIndex>\d+)/$',
        views.get_vendor_followers_subset, name='get_vendor_followers_subset'),
    url(r'^vendor_following_subset/(?P<content_type_id>\d+)/(?P<object_id>\d+)/(?P<sIndex>\d+)/(?P<lIndex>\d+)/$',
        views.get_vendor_following_subset, name='get_vendor_following_subset'),
)
