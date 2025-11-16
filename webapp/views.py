from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.generic import TemplateView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskListView(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'task_list.html', context)


class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs['pk'])
        context['task'] = task
        return context


class TaskCreateView(View):
    template_name = 'task_form.html'

    def get(self, request, *args, **kwargs):
        form = TaskForm()
        return render(request, self.template_name, {'form': form, 'title': 'Создать задачу'})

    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task()
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.save()
            task.task_type.set(form.cleaned_data.get('task_type'))
            return redirect('task_list')
        return render(request, self.template_name, {'form': form, 'title': 'Создать задачу'})


def task_update_view(request, pk, *args, **kwargs):
    task = get_object_or_404(Task, pk=pk)

    if request.method == "GET":
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'task_type': task.task_type.all(),
        })
        context = {
            'form': form,
            'task': task,
            'title': 'Редактировать задачу',
        }
        return render(request, 'task_form.html', context)

    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data.get('summary')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.save()
            task.task_type.set(form.cleaned_data.get('task_type'))
            return redirect('task_detail', pk=task.pk)

        context = {
            'form': form,
            'task': task,
            'title': 'Редактировать задачу',
        }
        return render(request, 'task_form.html', context)


def task_delete_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_confirm_delete.html', {'task': task})
    task.delete()
    return redirect('task_list')
