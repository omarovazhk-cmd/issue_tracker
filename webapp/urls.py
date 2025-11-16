from django.urls import path
from webapp.views import (TaskListView, TaskDetailView, TaskCreateView, task_update_view, task_delete_view)

urlpatterns = [
    path('', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task_detail'),
    path('tasks/add/', TaskCreateView.as_view(), name='task_add'),
    path('tasks/<int:pk>/edit/', task_update_view, name='task_edit'),
    path('tasks/<int:pk>/delete/', task_delete_view, name='task_delete'),
]
