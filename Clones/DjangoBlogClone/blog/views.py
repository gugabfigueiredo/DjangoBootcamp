# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from blog import models
from blog import forms

# Create your views here.


class AboutView(TemplateView):

    template_name = 'about.html'


class PostListView(ListView):

    model = models.Post

    def get_queryset(self):

        query = models.Post.objects.filter(publish_date__lte=timezone.now())

        return query.order_by('-publish_date')


class PostDetailView(DetailView):

    model = models.Post


class PostCreateView(LoginRequiredMixin, CreateView):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.PostForm

    model = models.Post


class PostUpdateView(LoginRequiredMixin, UpdateView):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'

    form_class = forms.PostForm

    model = models.Post


class PostDeleteView(LoginRequiredMixin, DeleteView):

    model = models.Post

    success_url = reverse_lazy('post_list')


class DraftListView(LoginRequiredMixin, ListView):

    login_url = '/login/'

    redirect_field_name = 'blog/post_list.html'

    model = models.Post

    def get_queryset(self):

        query = models.Post.objects.filter(publish_date__isnull=True)

        return query.order_by('-publish_date')


################################################
################################################


@login_required
def publish_post(request, pk):

    post = get_object_or_404(models.Post, pk=pk)
    post.publish()

    return redirect('post_detail', pk=pk)


@login_required
def add_comment(request, pk):

    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':

        form = forms.CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', pk=post.pk)

    else:

        form = forms.CommentForm()

    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def approve_comment(request, pk):

    comment = get_object_or_404(models.Comment, pk=pk)

    comment.approve()

    return redirect('post_detail', pk=comment.post.pk)


@login_required
def remove_comment(request, pk):

    comment = get_object_or_404(models.Comment, pk=pk)

    post_pk = comment.post.pk

    comment.delete()

    return redirect('post_detail', pk=post_pk)