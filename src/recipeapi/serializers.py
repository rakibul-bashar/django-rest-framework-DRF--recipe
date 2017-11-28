from .models import *

from django.contrib.auth import get_user_model #if use a custom user model otherwise model is User
from rest_framework import serializers
User=get_user_model()

class UserSerializer(serializers.HyperlinkedModelSerializer):

    recipes = serializers.HyperlinkedRelatedField(many=True, view_name='recipe-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'recipes')







class IngredientSerializer(serializers.ModelSerializer):
    #ingredients_nol=RecipeSerializer(many=True,read_only=True)

    class Meta:
        model = Ingredient
        fields = ('id', 'ingredient_name', 'ingredient_amount')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    ingredients_nol = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('url','id','owner', 'recipe_name', 'recipe_image_path', 'recipe_description','ingredients_nol')

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients_nol')
        recipe = Recipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredient.objects.create(recipe=recipe, **ingredients_data)
        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients_nol')
        instance.recipe_name = validated_data['recipe_name']
        instance.recipe_image_path = validated_data['recipe_image_path']
        instance.recipe_description = validated_data['recipe_description']

        for ingredient in ingredients_data:
            ingredient, created = Ingredient.objects.get_or_create(ingredient_name=ingredient['ingredient_name'])
            recipe.ingredients_nol.add(ingredient)
        return instance