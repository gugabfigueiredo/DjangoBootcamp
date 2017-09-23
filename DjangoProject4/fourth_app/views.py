# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.shortcuts import render

# Create your views here.


APP_DIR = os.path.basename(os.path.dirname(__file__))


def index(request):

    view_path = os.path.join(APP_DIR, 'index.html')

    context = {'text': 'hello world', 'number': 100}

    return render(request, view_path, context)


def other(request):

    view_path = os.path.join(APP_DIR, 'other.html')

    return render(request, view_path)


def relatives(request):

    view_path = os.path.join(APP_DIR, 'relative_url_templates.html')

    return render(request, view_path)


def base(request):

    view_path = os.path.join(APP_DIR, 'base.html')

    return render(request, view_path)