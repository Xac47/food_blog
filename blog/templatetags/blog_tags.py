from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag()
def get_categories_menu():
    return Category.objects.filter(parent__isnull=True).order_by('name')

@register.inclusion_tag('blog/include/tags/statistics_category.html')
def get_categories():
    categories = Category.objects.filter(parent__isnull=True).order_by('name')
    return {'categories': categories}