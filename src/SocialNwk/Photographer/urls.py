__author__ = 'leituo56'
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from Photographer import views
from django.conf.urls import include
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('',
    url(r'^$', views.home, name = 'home'),
    url(r'^signup/$', views.signup, name= 'signup'),
    url(r'^login/$',  views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^upload/$', views.upload, name = 'upload'),
    url(r'^explore/$', views.explore, name='explore'),
    url(r'^photo/(?P<pk>[0-9]+)/$', views.photo_page, name='photo_page'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.user_page, name='user_page'),
    url(r'^feed/$', views.feed, name='feed'),
    url(r'^find/$', views.find_friends, name='find_friends'),
    url(r'^stat/$', views.site_stat, name='site_stat'),

    url(r'^api/$', views.api_root, name='api_root'),
    url(r'^api/users/$', views.UserList.as_view(), name='user-list'),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
    url(r'^api/users/(?P<pk>[0-9]+)/follow/$', views.follow, name='user-follow'),
    url(r'^api/users/(?P<pk>[0-9]+)/unfollow/$', views.unfollow, name='user-unfollow'),
    url(r'^api/users/(?P<pk>[0-9]+)/stat/$', views.user_stat, name='user-stat'),
    url(r'^api/photos/$', views.PhotoList.as_view(), name='photo-list'),
    url(r'^api/photos/(?P<pk>[0-9]+)/$', views.PhotoDetail.as_view(), name='photo-detail'),
    url(r'^api/photos/stat/$', views.photo_stat, name='photo-stat'),

    url(r'^test/$', views.test, name = 'test')
)
urlpatterns = format_suffix_patterns(urlpatterns)