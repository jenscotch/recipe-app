from django.db import models

# Create your models here.

difficulty_level = (
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('intermediate', 'Intermediate'),
    ('hard', 'Hard'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.FloatField(help_text='in minutes')
    ingredients = models.CharField(max_length=500)
    difficulty = models.CharField(max_length=12, choices=difficulty_level, default='ez')

    def __str__(self):
        return str(self.name)