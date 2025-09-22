from django.db import models
from django.utils import timezone

# Create your models here.

class Manager(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)  # Store hashed password
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
