from django.db import models
from django.contrib.auth.models import User
from forum_login.models import CustomUser


class Thread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    region = models.CharField(max_length=100, default='Unknown')  # Add default value
    interest = models.CharField(max_length=100, default='General')  # Add default value

    def __str__(self):
        return self.title
