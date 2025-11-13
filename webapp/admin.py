from django.contrib import admin
from .models import Task, TaskStatus, TaskType


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "summary", "status", "task_type", "created_at", "updated_at")
    list_filter = ("status", "task_type")
    search_fields = ("summary", "description")
    fields = ("summary", "description", "status", "task_type", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
