# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from first_app.models import *

# Create your views here.


def index(request):

    wbpages = AccessRecord.objects.order_by('date')

    date_dic = {'access_records': wbpages}

    return render(request, 'first_app/index.html', context=date_dic)

    #return HttpResponse('This is the index page!')


def help(request):

    help_dic = {'help_me': 'This is me helping you!'}

    return render(request, 'first_app/help.html', context=help_dic)