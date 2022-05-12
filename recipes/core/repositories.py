from .models import Recipe


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
