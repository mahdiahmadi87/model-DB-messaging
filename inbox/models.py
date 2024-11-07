from django.db import models
from django.contrib.auth.models import User

class Inbox(models.Model):
    user = models.OneToOneField(User, related_name='inbox', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Inbox for {self.user}"
