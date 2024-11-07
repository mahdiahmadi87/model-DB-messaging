from django.db import models
from user.models import User
from messaging.models import Message
from notifications.models import Notification

class Inbox(models.Model):
    user = models.OneToOneField(User, related_name='inbox', on_delete=models.CASCADE)
    unread_messages = models.ManyToManyField(Message, blank=True)
    unread_notifications = models.ManyToManyField(Notification, blank=True)

    def __str__(self):
        return f"Inbox for {self.user}"
