"""URLs for Pasto"""
from django.conf.urls import patterns, url

urlpatterns = patterns('pasto',
    url(r'^$', 'views.home'),
)
