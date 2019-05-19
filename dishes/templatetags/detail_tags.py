from django import template
from dishes import models
register = template.Library()


@register.simple_tag
def get_dish_type():
    dtype = models.DishType.objects.all()
    return dtype


@register.simple_tag
def get_package_theme():
    ptheme = models.PackageTheme.objects.all()
    return ptheme


@register.simple_tag
def get_package_name():
    pname = models.Package.objects.all()
    return pname


@register.simple_tag
def get_dish_category():
    categorys = models.DishCategory.objects.all()
    return categorys