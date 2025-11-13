from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from webapp.models import Task
from webapp.forms import TaskForm


class TaskListView(TemplateView):
    template_name = 'task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all().order_by('-created_at')
        return context


class TaskDetailView(TemplateView):
    template_name = 'task_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs['pk'])
        context['task'] = task
        return context


class TaskCreateView(View):
    template_name = 'task_form.html'

    def get(self, request):
        form = TaskForm()
        return self.render(form)

    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return self.render(form)

    def render(self, form):
        from django.shortcuts import render
        return render(self.request, self.template_name, {'form': form, 'title': 'Создать задачу'})


class TaskUpdateView(View):
    template_name = 'task_form.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(instance=task)
        return self.render(form, task)

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', pk=task.pk)
        return self.render(form, task)

    def render(self, form, task):
        from django.shortcuts import render
        context = {
            'form': form,
            'task': task,
            'title': 'Редактировать задачу',
        }
        return render(self.request, self.template_name, context)


class TaskDeleteView(View):
    template_name = 'task_confirm_delete.html'

    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        from django.shortcuts import render
        return render(request, self.template_name, {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect('task_list')
