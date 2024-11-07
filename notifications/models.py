from django.db import models
from inbox.models import Inbox

class Notification(models.Model):
    user = models.ManyToManyField(Inbox, blank=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user} - {self.timestamp}"
