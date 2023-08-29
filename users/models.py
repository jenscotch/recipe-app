from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=120, default='no name...')
    bio = models.TextField(default='no bio...')

    def __str__(self):
        return str(f"Profile of {self.name}")