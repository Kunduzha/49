from webapp.views import IndexView_project, ListView, Add_list, List_update, Delete_list, ProjectView, IndexView, \
    Add_project, ProjectUpdate, Delete_Project
from django.urls import path

app_name = 'project'

urlpatterns = [

    path('', IndexView_project.as_view(), name='main_page'),
    path('project/<int:pk>/', ProjectView.as_view(), name='more'),
    path('add/', Add_project.as_view(), name='adding'),
    path('update/<int:pk>/project/', ProjectUpdate.as_view(), name='update'),
    path('delete/<int:pk>/project/', Delete_Project.as_view(), name='delete'),
    path('<int:pk>/add_list/', Add_list.as_view(), name='adding_list'),
    path('list/<int:pk>/', ListView.as_view(), name='list_more'),
    path('delete/<int:pk>/', Delete_list.as_view(), name='delete_list'),
    path('update/<int:pk>/', List_update.as_view(), name='list_update'),

]
