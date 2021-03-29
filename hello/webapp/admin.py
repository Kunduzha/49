from django.contrib import admin
from webapp.models import List, Status, Types, Project


# Register your models here.
# class ListAdmin(admin.ModelAdmin):


# class ListAdmin(admin.ModelAdmin):
#     list_display = ['id', 'status', 'description', 'about_list']
#     list_filter = ['description']
#     search_fields = ['status', 'description']
#     fields = ['id', 'status', 'description', 'about_list', 'types']
#     readonly_fields = ['created_at', 'id']


# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'description', 'begin_at', 'created_at']
#     list_filter = ['description']
#
#     fields = ['id', 'title', 'description', 'begin_at', 'created_at']

admin.site.register(Project)
# admin.site.register(Status)
# admin.site.register(Types)