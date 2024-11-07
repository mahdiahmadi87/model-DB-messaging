# inbox/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Inbox

@receiver(post_save, sender=User)
def create_inbox_for_new_user(sender, instance, created, **kwargs):
    if created:
        Inbox.objects.create(user=instance)
