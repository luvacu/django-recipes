from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .repositories import RecipesRepository
from .serializers import RecipeSerializer


class RecipesView(APIView):

    def get(self, request):
        query_param_name = request.GET.get('name')
        if query_param_name:
            recipe_dtos = RecipesRepository.get_recipes(name=query_param_name)
        else:
            recipe_dtos = RecipesRepository.get_recipes_all()
        serializer = RecipeSerializer(recipe_dtos, many=True)
        return Response(data=serializer.data)


class RecipeDetailView(APIView):

    def get(self, request, recipe_pk):
        recipe_dto = RecipesRepository.get_recipe(pk=recipe_pk)
        if not recipe_dto:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RecipeSerializer(recipe_dto)
        return Response(data=serializer.data)
