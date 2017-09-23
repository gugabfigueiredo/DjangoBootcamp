# -*- coding: utf-8 -*-

from django import forms
#from django.core import validators
from . import models


class UserModelForm(forms.ModelForm):

    class Meta():

        model = models.User

        fields = '__all__'

        exclude = ['full_name']
