from django.contrib import admin
from .models import Task, Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ('project_title', 'author')
    list_display = ("project_title", "author")
    
    ordering = ["-project_title"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    search_fields = ('status', 'priority', 'priority')
    list_filter = ('project', 'task_author', 'status', 'priority')
    list_display = ('project', 'task', 'task_author', 'status', 'priority')
    ordering = ["priority"]