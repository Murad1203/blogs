from django import template

from blg.models import Category

register = template.Library()


@register.simple_tag()
def get_category():
    return Category.objects.all()


@register.inclusion_tag('blg/list_category.html')
def show_category():
    categories = Category.objects.all()
    return {'categories': categories}
