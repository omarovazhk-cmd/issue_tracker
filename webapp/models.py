from django.db import models


class TaskStatus(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Тип задачи"
        verbose_name_plural = "Типы задач"

    def __str__(self):
        return self.name


class Task(models.Model):
    summary = models.CharField(max_length=255, verbose_name="Краткое описание")
    description = models.TextField(blank=True, verbose_name="Полное описание")

    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, verbose_name="Статус")

    task_type = models.ForeignKey(TaskType, on_delete=models.PROTECT, verbose_name="Тип задачи")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.summary
