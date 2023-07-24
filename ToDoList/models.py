from django.db import models

# Create your models here.


class Task(models.Model):
    # The model used to represent a Task
    # The deleted field indicates whether a task was deleted so the user can also see deleted tasks
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000)
    completed = models.BooleanField(null=True, default=False)
    deleted = models.BooleanField(null=True, default=False)

