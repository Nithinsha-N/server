import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone


class Status(models.IntegerChoices):
    TODO = 0, 'TODO'
    IN_PROGRESS = 1, 'IN_PROGRESS'
    DONE = 2, 'DONE'


class Ticket(models.Model):
    title = models.CharField(max_length=200)
    desc = models.CharField(max_length=2000)
    created_time = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="created_by")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="assignee")
    Status = models.IntegerField(default=Status.TODO, choices=Status.choices)

    def __str__(self):
        return f"{self.title}"
