__author__ = 'leituo56'
from django.conf.urls import patterns, url
from django.contrib.auth.views import login, logout
from Photographer import views

urlpatterns = patterns('',
    url(r'^$', views.home, name = 'home'),
    url(r'^signup/$', views.signup, name= 'signup'),
    url(r'^login/$',  views.login_view, name = 'login'),
    url(r'^logout/$', views.logout_view, name = 'logout'),
    url(r'^upload/$', views.upload, name = 'upload'),

    url(r'^test/$', views.test, name = 'test')
)