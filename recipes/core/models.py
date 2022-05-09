from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=80)

class Recipe(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient)
