from django import forms
from django.forms import widgets

from webapp.models import Status, Type


class ListForms(forms.Form):
    type = forms.ModelChoiceField(required=False, queryset=Type.objects.all(), label='type')
    status = forms.ModelChoiceField(required=False, queryset=Status.objects.all(), label='status')
    title = forms.CharField(max_length=50, required=True, label='title')
    description = forms.CharField(max_length=200, min_length=5, required=True, label='description')
    about_list = forms.CharField(max_length=3000, required=False, label='about_list', widget=widgets.Textarea)