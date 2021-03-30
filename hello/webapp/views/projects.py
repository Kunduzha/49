from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
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

# class ProjectUpdate(TemplateView):
#     template_name = 'projects/update.html'
#
#     def get_context_data(self, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs.get("pk"))
#         form = ProjectForms(initial={
#             'title': project.title,
#             'description': project.description,
#             'begin_at': project.begin_at,
#             'end_at': project.end_at,
#         })
#         kwargs['form'] = form
#         kwargs['project'] = project
#         return super().get_context_data(**kwargs)
#
#     def post(self, request, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs.get("pk"))
#         form = ProjectForms(data=request.POST)
#         if form.is_valid():
#             project.title = form.cleaned_data["title"]
#             project.description = form.cleaned_data["description"]
#             project.begin_at = form.cleaned_data["begin_at"]
#             project.end_at = form.cleaned_data['end_at']
#             project.save()
#             return redirect('project_more', pk=project.pk)
#         else:
#             return render(request, 'projects/update.html', context={'form': form, 'project': project})

class ProjectUpdate(UpdateView):
    model = Project
    template_name = 'projects/update.html'
    form_class = ProjectForms
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('project_more', kwargs={'pk': self.object.pk})

# class Delete_Project(View):
#     def get(self, request, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs.get('pk'))
#         return render(request, 'projects/delete.html', context={'project': project})
#
#     def post(self, request, **kwargs):
#         project = get_object_or_404(Project, pk=kwargs.get('pk'))
#         project.delete()
#         return redirect('main_page')

class Delete_Project(DeleteView):
    template_name = 'projects/delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('main_page')