from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, RedirectView, ListView

from webapp.models import List, Types
from webapp.forms import ListForms


class IndexView(ListView):
    model = List
    template_name = 'index.html'
    context_object_name = 'lists'
    paginate_by = 10
    paginate_orphans = 5
    # def get_context_data(self, **kwargs):
    #     print(kwargs)
    #     kwargs['lists'] = List.objects.all()
    #     print(kwargs)
    #     return super().get_context_data(**kwargs)

    def get_queryset(self):
        return List.objects.all().order_by(-'created_at')


class ListView(TemplateView):

    template_name = 'list_view.html'

    def get_context_data(self, **kwargs):
        kwargs['list'] = get_object_or_404(List, id=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class Add_list(View):
    def get(self, request):
        form = ListForms()
        return render(request, 'add_list.html', {'form': form})

    def post(self, request):
        form = ListForms(data=request.POST)
        if form.is_valid():
            status = form.cleaned_data["status"]
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            about_list = form.cleaned_data['about_list']
            new_list = List.objects.create(status=status, description=description, title=title,
                                           about_list=about_list)
            new_list.types.set(form.cleaned_data["types"])
            return redirect('list_more', pk=new_list.pk)
        else:
            return render(request, 'add_list.html', {'form': form})

class List_update(TemplateView):
    template_name = 'listupdate.html'

    def get_context_data(self, **kwargs):
        list = get_object_or_404(List, pk=kwargs.get("pk"))
        form = ListForms(initial={
            'types': list.types.all(),
            'title': list.title,
            'description': list.description,
            'status': list.status,
            'created_at': list.created_at,
            'about_list': list.about_list,
        })
        kwargs['form'] = form
        kwargs['list'] = list
        return super().get_context_data(**kwargs)

    def post(self, request, **kwargs):
        list = get_object_or_404(List, pk=kwargs.get("pk"))
        form = ListForms(data=request.POST)
        if form.is_valid():
            list.title = form.cleaned_data["title"]
            list.status = form.cleaned_data["status"]
            list.description = form.cleaned_data["description"]
            list.about_list = form.cleaned_data['about_list']
            list.save()
            types = form.cleaned_data["types"]
            list.types.set(types)
            return redirect('list_more', pk=list.pk)
        else:
            return render(request, 'listupdate.html', context={'form': form, 'list': list})


class Delete_list(View):
    def get(self, request, **kwargs):
        list = get_object_or_404(List, pk=kwargs.get('pk'))
        return render(request, 'delete.html', context={'list': list})
    def post(self, request, **kwargs):
        list = get_object_or_404(List, pk=kwargs.get('pk'))
        list.delete()
        return redirect('main_page')
