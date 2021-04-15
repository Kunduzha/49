# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect,
from django.contrib.auth import login
from django.shortcuts import render, redirect

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


