from django.contrib import admin
from webapp.models import Task, TaskStatus, TaskType


@admin.register(TaskStatus)
class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(TaskType)
class TaskTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'get_task_types', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'task_type')
    fields = ("summary", "description", "status", "task_type", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")

    def get_task_types(self, obj):
        return ", ".join(task.name for task in obj.task_type.all())

    get_task_types.short_description = "Типы задачи"
