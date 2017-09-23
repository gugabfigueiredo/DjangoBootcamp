# -*- coding: utf-8 -*-
from django.conf.urls import url
import os

from . import views


app_name = os.path.basename(os.path.dirname(__file__))

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^index/', views.index, name='index'),
    url(r'^other/', views.other, name='other'),
    url(r'^relatives/', views.relatives, name='relatives'),
    url(r'^base/', views.base, name='base')
]