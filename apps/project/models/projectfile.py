# apps/project/models/projectfile.py

from django.db import models

class ProjectFile(models.Model):
    objects = models.Manager()
    file = models.FileField(upload_to='project_files/')
    project = models.ForeignKey('Project', on_delete=models.CASCADE, related_name='project_files')

    def __str__(self):
        return self.file.name