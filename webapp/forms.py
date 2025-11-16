from django import forms
from django.forms import widgets
from webapp.models import Task, TaskStatus, TaskType
from webapp.validation import validate

from webapp.validation import validate


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

    def clean(self):
        cleaned_data = super().clean()
        errors = validate(cleaned_data)
        for field_name, error_message in errors.items():
            self.add_error(field_name, error_message)

        return cleaned_data
