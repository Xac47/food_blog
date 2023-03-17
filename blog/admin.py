from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from . import models

class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'auther', 'create_at', 'id')
    ordering = ('-id',)
    inlines = (RecipeInline,)


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'prep_time', 'cook_time', 'post')
    ordering = ('-id',)


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('message', 'name', 'email', 'post')
    ordering = ('-id',)


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
