# apps/project/models/project.py

from django.db import models
from apps.project.models.projectfile import ProjectFile

class Project(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=255)
    description = models.TextField()
    files = models.ManyToManyField(ProjectFile, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def count_of_files(self):
        return self.files.count()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']