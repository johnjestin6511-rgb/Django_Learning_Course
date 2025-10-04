from django import template

register =template.Library()
@register.filter("cut")

def cut(value,arg):
    '''
    This cout out all value of "arg" from the string
    '''
    return value.replace(arg,"")

# register.filter("cut",cut)