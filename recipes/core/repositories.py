from .models import Recipe, Ingredient
from django.db import transaction


class RecipesRepository:

    @staticmethod
    def get_recipes_all():
        recipes = Recipe.objects.all()
        return [recipe.to_dto() for recipe in recipes]

    @staticmethod
    def get_recipes(name):
        recipes = Recipe.objects.filter(name__icontains=name)
        return [recipe.to_dto() for recipe in recipes]

    @staticmethod
    def get_recipe(pk):
        try:
            recipe = Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            return None
        return recipe.to_dto()

    @staticmethod
    def create_recipe_and_ingredients(recipe: dict, ingredients: list):
        with transaction.atomic():
            ingredient_objects = [Ingredient(**ingredient) for ingredient in ingredients]
            created_ingredients = Ingredient.objects.bulk_create(ingredient_objects)
            created_recipe = Recipe.objects.create(**recipe)
            created_recipe.ingredients.set(created_ingredients)

        return created_recipe.to_dto()

    @staticmethod
    def create_recipe_with_ingredient_pks(recipe: dict, ingredient_pks: list):
        with transaction.atomic():
            ingredients = Ingredient.objects.filter(pk__in=ingredient_pks)
            created_recipe = Recipe.objects.create(recipe)
            created_recipe.ingredients.set(ingredients)

        return created_recipe.to_dto()
