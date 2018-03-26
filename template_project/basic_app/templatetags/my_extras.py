from django import template

register = template.Library()

def mycut(value, arg):
    """
    This cuts out all values for "arg" from the string!
    """
    return value.replace(arg,'')

register.filter('mycut', mycut)
