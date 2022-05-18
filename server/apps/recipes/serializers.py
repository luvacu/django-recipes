from rest_framework import serializers


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()


class RecipeSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    ingredients = IngredientSerializer(many=True)


class FullRecipeSerializer(RecipeSerializer):
    id = serializers.CharField()
