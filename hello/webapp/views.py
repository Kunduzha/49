from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView

from webapp.models import List
# from webapp.forms import ListForm, ListDeleteForm


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs['lists'] = List.objects.all()
        return super().get_context_data(**kwargs)


class ListView(TemplateView):

    template_name = 'list_view.html'

    def get_context_data(self, **kwargs):
        kwargs['list'] = get_object_or_404(List, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)