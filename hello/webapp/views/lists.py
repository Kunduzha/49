from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, TemplateView, RedirectView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from webapp.models import List, Types, Project
from webapp.forms import ListForms, SimpleSearchForm



class IndexView(ListView):
    model = List
    template_name = 'projects/index.html'
    context_object_name = 'lists'


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

        # return List.objects.all().order_by('-created_at')


class ListView( TemplateView):

    template_name = 'lists/list_view.html'

    def get_context_data(self, **kwargs):
        kwargs['list'] = get_object_or_404(List, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class Add_list(PermissionRequiredMixin, CreateView):
    # def get(self, request):
    #     form = ListForms()
    #     return render(request, 'lists/add.html', {'form': form})
    #
    # def post(self, request):
    #     form = ListForms(data=request.POST)
    #     if form.is_valid():
    #         status = form.cleaned_data["status"]
    #         title = form.cleaned_data["title"]
    #         description = form.cleaned_data["description"]
    #         about_list = form.cleaned_data['about_list']
    #         new_list = List.objects.create(status=status, description=description, title=title,
    #                                        about_list=about_list)
    #         new_list.types.set(form.cleaned_data["types"])
    #         return redirect('list_more', pk=new_list.pk)
    #     else:
    #         return render(request, 'lists/add.html', {'form': form})

    model = List
    template_name = 'lists/add.html'
    form_class = ListForms
    permission_required = 'webapp.add_list'
    permission_denied_message = 'У Вас нет разрешения на добавление задачи'

    def has_permission(self):
        return super().has_permission() and self.request.user in Project.objects.get(pk=self.kwargs.get('pk')).user.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk = self.kwargs.get('pk'))
        list = form.save(commit=False)
        list.project = project
        list.save()
        form.save_m2m()
        return redirect('project:more', pk = project.pk)


# class List_update(TemplateView):
#     template_name = 'lists/update.html'
#
#     def get_context_data(self, **kwargs):
#         list = get_object_or_404(List, pk=kwargs.get("pk"))
#         form = ListForms(initial={
#             'types': list.types.all(),
#             'title': list.title,
#             'description': list.description,
#             'status': list.status,
#             'created_at': list.created_at,
#             'about_list': list.about_list,
#         })
#         kwargs['form'] = form
#         kwargs['list'] = list
#         return super().get_context_data(**kwargs)
#
#     def post(self, request, **kwargs):
#         list = get_object_or_404(List, pk=kwargs.get("pk"))
#         form = ListForms(data=request.POST)
#         if form.is_valid():
#             list.title = form.cleaned_data["title"]
#             list.status = form.cleaned_data["status"]
#             list.description = form.cleaned_data["description"]
#             list.about_list = form.cleaned_data['about_list']
#             list.save()
#             types = form.cleaned_data["types"]
#             list.types.set(types)
#             return redirect('project_more', pk=list.project.pk)
#         else:
#             return render(request, 'lists/update.html', context={'form': form, 'list': list})


class List_update(PermissionRequiredMixin, UpdateView):
    model = List
    template_name = 'lists/update.html'
    form_class= ListForms
    context_object_name = 'list'
    permission_required = 'webapp.change_list'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.object.project.user.all()

    def get_success_url(self):
        return reverse('project:more', kwargs={'pk': self.object.project.pk})

# class Delete_list(View):
#     def get(self, request, **kwargs):
#         list = get_object_or_404(List, pk=kwargs.get('pk'))
#         return render(request, 'lists/delete.html', context={'list': list})
#     def post(self, request, **kwargs):
#         list = get_object_or_404(List, pk=kwargs.get('pk'))
#         list.delete()
#         return redirect('main_page')

class Delete_list(PermissionRequiredMixin, DeleteView):
    model = List
    permission_required = 'webapp.delete_list'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.object.project.user.all()
    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('project:more', kwargs={'pk': self.object.project.pk})
