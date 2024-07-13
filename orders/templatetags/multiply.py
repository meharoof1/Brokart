from django import template

register=template.Library() # To register
@register.simple_tag(name='multiply') # Add as decorator , name='multiply' is the name should load in the template 
def multiply(a,b):
    return a*b