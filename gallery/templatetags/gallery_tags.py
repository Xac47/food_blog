from django import template
from gallery.models import Gallery

register = template.Library()

@register.inclusion_tag('gallery/include/tags/slider.html')
def slider():
    slider = Gallery.objects.order_by('name')[:5]
    return {'images': slider}