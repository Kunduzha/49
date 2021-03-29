from django.shortcuts import render, get_object_or_404, redirect,reverse
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView, CreateView
from django.db.models import Q
from django.utils.http import urlencode

from webapp.models import Project
from webapp.forms import ListForms, SimpleSearchForm, ProjectForms

class IndexView_project(ListView):
    model = Project
    template_name = 'projects/index.html'
    context_object_name = 'projects'
    paginate_by = 3
    paginate_orphans = 1


    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, object_list = None, **kwargs):
        context = super().get_context_data(object_list= object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(title__icontains=self.search_value)  | Q(description__icontains=self.search_value)
            queryset = queryset.filter(query)
        return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class ProjectView(DetailView):
    model = Project
    template_name = 'projects/project_view.html'


class Add_project(CreateView):
    template_name = 'projects/create.html'
    model = Project
    form_class = ProjectForms

    def get_success_url(self):
        return reverse('project_more', kwargs = {'pk': self.object.pk})
