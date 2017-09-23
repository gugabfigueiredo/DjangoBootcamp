# -*- coding: utf-8 -*-

from django.conf.urls import url

from second_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^users/', views.users, name='users'),
    url(r'^forms_page/', views.forms_page, name='forms'),
]