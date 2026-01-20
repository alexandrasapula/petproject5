from django.db import models
from django.conf import settings
from datetime import date


class Device(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='devices')
    name = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, null=True, blank=True, unique=True)
    start_date = models.DateField(null=True, blank=True)
    manual = models.FileField(upload_to='manuals/', blank=True, null=True)
    has_embeddings = models.BooleanField(default=False)

    @property
    def worked_days(self):
        if self.start_date:
            return (date.today() - self.start_date).days
        return None

    def display_name(self):
        return self.name if self.name else self.model

    def __str__(self):
        return f"{self.display_name()} ({self.user.username})"
