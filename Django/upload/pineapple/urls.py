from django.conf.urls import patterns, url
from pineapple import views

urlpatterns = patterns('',
        url(r'^upload_csv', views.upload, name = 'upload'),
        )