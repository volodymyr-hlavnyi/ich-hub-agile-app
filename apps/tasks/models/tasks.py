from django.db import models

from apps.tasks.models.tag import Tag
from apps.tasks.choices import Priority, Statuses


class Task(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(blank=False)
    status = models.CharField(
        max_length=15,
        choices=Statuses.choices,
        default=Statuses.NEW.value
    )
    priority = models.IntegerField(
        choices=Priority.choices,
        default=Priority.MEDIUM.value
    )
    tags = models.ManyToManyField(Tag, related_name="tasks")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["due_date"]
