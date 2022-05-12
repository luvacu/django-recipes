from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .repositories import RecipesRepository
from .serializers import RecipeSerializer, FullRecipeSerializer


class RecipesView(APIView):

    def get(self, request):
        query_param_name = request.GET.get('name')
        if query_param_name:
            recipe_dtos = RecipesRepository.get_recipes(name=query_param_name)
        else:
            recipe_dtos = RecipesRepository.get_recipes_all()
        serializer = FullRecipeSerializer(recipe_dtos, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        request_serializer = RecipeSerializer(data=request.data)
        request_serializer.is_valid(raise_exception=True)
        ingredients = request_serializer.validated_data.pop('ingredients')
        recipe = request_serializer.validated_data
        recipe_dto = RecipesRepository.create_recipe_and_ingredients(recipe=recipe, ingredients=ingredients)
        response_serializer = FullRecipeSerializer(recipe_dto)
        return Response(data=response_serializer.data)


class RecipeDetailView(APIView):

    def get(self, request, recipe_pk):
        recipe_dto = RecipesRepository.get_recipe(pk=recipe_pk)
        if not recipe_dto:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FullRecipeSerializer(recipe_dto)
        return Response(data=serializer.data)
