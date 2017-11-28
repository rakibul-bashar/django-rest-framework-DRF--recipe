from django.db import models


# Create your models here.

class Recipe(models.Model):
    owner=models.ForeignKey('auth.User',related_name='recipes',on_delete=models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    recipe_image_path = models.URLField(max_length=200, blank=False)
    recipe_description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.recipe_name

class Ingredient(models.Model):

    recipe = models.ForeignKey(Recipe, related_name='ingredients_nol', on_delete=models.CASCADE,null=True,blank=True)
    ingredient_name = models.CharField(max_length=128, blank=True, null=False)
    ingredient_amount = models.IntegerField(blank=True, null=False)
    timeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.ingredient_name