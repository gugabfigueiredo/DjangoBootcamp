# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    View,
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from sixth_app import models

import os

APP_DIR = os.path.basename(os.path.dirname(__file__))


# Create your views here.
def index(request):

    context = {}

    view_path = os.path.join(APP_DIR, 'index.html')

    return render(request, view_path, context)


class CBView(View):

    def get(self, request):

        return HttpResponse('Class Based Views Are Cool!')


class DJTemplateView(TemplateView):

    template_name = os.path.join(APP_DIR, 'template_view.html')

    def get_context_data(self, **kwargs):

        context = super(DJTemplateView, self).get_context_data(**kwargs)

        context['injectme'] = 'BASIC INJECTION!'

        return context


class SchoolListView(ListView):

    model = models.School

    #template_name = os.path.join(APP_DIR, '#.html')


class SchoolDetailView(DetailView):

    context_object_name = 'school_detail'

    model = models.School

    template_name = os.path.join(APP_DIR, 'school_detail.html')


class SchoolCreateView(CreateView):

    fields = ('name', 'principal', 'location')

    model = models.School


class SchoolUpdateView(UpdateView):

    fields = ('name', 'principal')

    model = models.School


class SchoolDeleteView(DeleteView):

    model = models.School

    success_url = reverse_lazy('sixth_app:list')