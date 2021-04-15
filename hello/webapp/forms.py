from django import forms
from webapp.models import List, Project
from django.forms import widgets

from webapp.models import Status, Types


# class ListForms(forms.ModelForm):
#     types = forms.ModelMultipleChoiceField(required=False, queryset=Types.objects.all(), label='types')
#     status = forms.ModelChoiceField(required=False, queryset=Status.objects.all(), label='status')
#     title = forms.CharField(max_length=50, required=True, label='title')
#     description = forms.CharField(max_length=200, min_length=5, required=True, label='description')
#     about_list = forms.CharField(max_length=3000, required=False, label='about_list', widget=widgets.Textarea)
#

class ListForms(forms.ModelForm):

    class Meta:
        model=List
        fields = ['types', 'status', 'title', 'description', 'about_list']

class SimpleSearchForm(forms.Form):

    search = forms.CharField(max_length=100, required=False, label="Найти")


class ProjectForms(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['begin_at', 'end_at', 'title', 'description']


class ProjectUserForms(forms.ModelForm):

    class Meta:
        model = Project
        fields = ['user']
