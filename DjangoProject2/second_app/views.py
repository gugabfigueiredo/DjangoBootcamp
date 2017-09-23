# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.shortcuts import render

from . import models, forms

# Create your views here.


APP_DIR = os.path.dirname(__file__).split('/').pop()


def index(request):

    #idx_dic = {}

    view_path = os.path.join(APP_DIR, 'index.html')

    return render(request, view_path)


def users(request):

    view_path = os.path.join(APP_DIR, 'users.html')

    usr_list = models.User.objects.order_by('first_name')

    user_dic = {'users': usr_list}

    return render(request, view_path, context=user_dic)


def forms_page(request):

    view_path = os.path.join(APP_DIR, 'forms.html')

    form = forms.UserModelForm()

    if request.method == 'POST':

        form = forms.UserModelForm(request.POST)

        if form.is_valid():

            form.save(commit=True)
            return index(request)

        else:
            print 'ERROR: INVALID FORM'

    return render(request, view_path, {'form': form})


#if __name__ == '__main__':

    #print(os.path.dirname(os.path.abspath(__file__)).split('/').pop())
