from django.contrib.auth.models import User
from django.db import models

from apps.tasks.models.tag import Tag
from apps.tasks.choices import Priority, Statuses

from apps.tasks.utils.set_datetime import last_day_of_month

class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=False)
    status = models.CharField(
        max_length=15,
        choices=Statuses.choices,
        default=Statuses.NEW.value
    )
    priority = models.SmallIntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM.value[0]
    )
    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="tasks"
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.PROTECT, related_name="assigned_tasks", blank=True, null=True)

    def __str__(self):
        return self.name, self.status

    class Meta:
        ordering = ["-deadline"]
        unique_together = (("name", "project"),)
