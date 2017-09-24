# -*- coding: utf-8 -*-

from django.conf.urls import url

from blog import views


urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    url(r'^post/new/$', views.PostCreateView.as_view(), name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_edit'),
    url(r'^post/(?P<pk>\d+)/rmv/$', views.PostDeleteView.as_view(), name='post_remove'),
    url(r'^drafts/$', views.DraftListView.as_view(), name='drafts'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.approve_comment, name='apprv_comment'),
    url(r'^comment/(?P<pk>\d+)/rmv/$', views.approve_comment, name='rmv_comment'),
    url(r'^post/(?P<pk>\d+)/pub/$', views.publish_post, name='pub_post'),
]