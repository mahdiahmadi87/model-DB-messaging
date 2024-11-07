from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.username

class Contact(models.Model):
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    contact_user = models.ForeignKey(User, related_name='contacted_by', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.contact_user}"
