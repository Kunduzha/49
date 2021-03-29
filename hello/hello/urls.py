"""hello URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import IndexView_project, ListView,  Add_list, List_update, Delete_list, ProjectView, IndexView, Add_project, ProjectUpdate, Delete_Project


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView_project.as_view(), name='main_page'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_more'),
    path('add/', Add_project.as_view(), name='adding_project'),
    path('update/<int:pk>/project/', ProjectUpdate.as_view(), name='project_update'),
    path('delete/<int:pk>/project/', Delete_Project.as_view(), name='delete_project'),
    path('<int:pk>/add_list/', Add_list.as_view(), name='adding_list'),
    path('list/<int:pk>/', ListView.as_view(), name='list_more'),
    path('delete/<int:pk>/', Delete_list.as_view(), name='delete_list'),
    path('update/<int:pk>/', List_update.as_view(), name='list_update')
]
