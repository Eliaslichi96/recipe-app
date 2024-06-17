from django.db import models

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    cooking_time = models.IntegerField()
    description = models.TextField()
    difficulty = models.CharField(max_length=50)

    def __str__(self):
        return self.name
