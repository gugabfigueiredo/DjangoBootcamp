# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from . import forms
# Create your views here.


def index(request):

    return render(request, 'third_app/index.html')


def form_name_view(request):

    form = forms.FormName()

    if request.method == 'POST':

        form = forms.FormName(request.POST)

        if form.is_valid():

            # DO SOMETHING CODE

            print "VALIDATION SUCCESS"

            for key, value in form.cleaned_data.iteritems():
                print key + ':', value

    return render(request, 'third_app/form_page.html', {'form': form})