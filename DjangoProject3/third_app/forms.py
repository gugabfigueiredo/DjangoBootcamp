# -*- coding: utf-8 -*-

from django import forms
from django.core import validators
from . import models

#def check_for_z(value):

    #if value[0].lower() =! 'z':
        #raise forms.ValidationError("NAME NEEDS TO START WITH Z")


class FormName(forms.Form):
    '''
    This is my form
    '''

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')

    #text = forms.CharField(widget=forms.Textarea)

    #botchatcher = forms.CharField(
        #required=False,
        #widget=forms.HiddenInput,
        ##validators=[validators.MaxLengthValidator(0)]
    #)


class ModelForm(forms.ModelForm):

    '''
    This is my other form
    '''

    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField()

    class Meta:

        model = MyModel

        # list of fields to include, "__all__" to include all fields
        fields =

        # list of fields to exclude
        exclude = []