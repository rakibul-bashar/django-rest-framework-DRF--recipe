from django.contrib import admin
from recipeapi.models import Recipe,Ingredient
# Register your models here.


admin.site.register(Recipe)
admin.site.register(Ingredient)