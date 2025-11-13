from django import forms
from .models import Task, TaskStatus, TaskType


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=TaskStatus.objects.all(),
        label="Статус"
    )
    task_type = forms.ModelMultipleChoiceField(
        queryset=TaskType.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label="Типы задачи"
    )

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'task_type')
        widgets = {'summary': forms.TextInput(attrs={'class': 'form-control'}),
                   'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                   }
