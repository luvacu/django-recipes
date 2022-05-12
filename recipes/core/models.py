from django.db import models
from .dtos import RecipeDTO, IngredientDTO


class Ingredient(models.Model):
    name = models.CharField(max_length=80)

    def to_dto(self):
        return IngredientDTO(name=self.name)


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=1000)
    ingredients = models.ManyToManyField(Ingredient)

    def to_dto(self):
        ingredient_dtos = [ingredient.to_dto() for ingredient in self.ingredients.all()]
        return RecipeDTO(
            id=str(self.id),
            name=self.name,
            description=self.description,
            ingredients=ingredient_dtos
        )
