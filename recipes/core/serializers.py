from rest_framework import serializers


class IngredientSerializer(serializers.Serializer):
    name = serializers.CharField()


class RecipeSerializer(serializers.Serializer):
    id = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    ingredients = IngredientSerializer(many=True)
