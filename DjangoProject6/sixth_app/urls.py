# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

from sixth_app import views

import os

app_name = os.path.basename(os.path.dirname(__file__))

urlpatterns = [
    url(r'^cbv/$', views.CBView.as_view(), name='class'),
    url(r'^tv/$', views.DJTemplateView.as_view(), name='template'),
    url(r'^lv/$', views.SchoolListView.as_view(), name='list'),
    url(r'^lv/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
    url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
    url(r'^lv/update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
    url(r'^lv/delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]
