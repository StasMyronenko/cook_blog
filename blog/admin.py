from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.


class RecipeInline(admin.StackedInline):  # возможность создавать рецепты прямо во время создания блюда
    model = models.Recipe
    extra = 1  # количество рецептов


class PostAdmin(admin.ModelAdmin):  # пишем коректные названия способ 1
    list_display = ['title', 'category', 'author', 'create_at', 'id']
    inlines = [RecipeInline]  # поключаем таблицу рецептов к таблице блюд

    # для копирования постов
    save_as = True
    save_on_top = True  # что бы кнопка сохранения была сверху


@admin.register(models.Recipe)  # пишем коректные названия способ 2, в этом случае не нужно ниже отдельно подключать модель
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cook_time', 'prep_time', 'post']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)