# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect,
from django.contrib.auth import login, get_user_model
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from accounts.forms import MyUserCreationForm


# Create your views here.

# def login_view(request):
#     context = {}
#     print('пустой контекст', context)
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         print('username=', username)
#         password = request.POST.get('password')
#         user = authenticate(request, username = username, password = password)
#         print('принтую user', user)
#         if user is not None:
#             login(request, user)
#             print('Принтую login', login)
#             return redirect('article_index')
#         else:
#             context['has_error'] = True
#             print(context['has_error'])
#     return render(request, 'login.html', context = context)
#     print(context)
#
# def logout_view(request):
#     logout(request)
#     return redirect('main_page')

# class LoginView(LoginView):
#     context = {}
#         if request.method == 'POST':
#             username  = request.POST.get('username')
#             password = request.POST.get('password')
#             user = authenticate(request, username = username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('main_page')
#             else:
#                 context['has_error'] = True
#         return render(request, 'registration/login.html', context = context)
#
#
# class LogoutView(LogoutView):
#     logout(request)
#     return redirect('main_page')


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('project:main_page')
    else:
        form = MyUserCreationForm()
    return render(request, 'registration/user_create.html', context = {'form':form})

class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_related_by = 5
    paginate_related_orphans = 0

    def get_context_data(self, **kwargs):
        projects = self.get_object().projects.all()
        paginator = Paginator(projects, self.paginate_related_by, orphans= self.paginate_related_orphans)
        page_number = self.request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        kwargs['page_obj'] = page
        kwargs['projects'] = page.object_list
        kwargs['is_paginated'] = page.has_other_pages()
        return super().get_context_data(**kwargs)





