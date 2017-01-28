from django.conf.urls import patterns, url
from pineapple import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name= 'about'),
        url(r'^menu/', views.menu, name= 'menu'),
        url(r'^order/', views.order, name= 'order'),
        url(r'^contact/', views.contact, name='contact'),
        url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^add_category/$', views.add_category, name='add_category'),
	url(r'^add_page/(?P<category_name_slug>[\w\-]+)/$', views.add_page, name='add_page'),		
        url(r'^display/', views.display, name= 'display'),
        url(r'^page/(?P<page_name_slug>[\w\-]+)/$', views.page, name='category'),
        url(r'^upload_csv', views.upload, name = 'upload'),
        )