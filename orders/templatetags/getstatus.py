from django import template

register=template.Library() # To register

@register.simple_tag(name='getstatus') # Add as decorator , name='gettotal' is the name should load in the template 


def getstatus(status):
    status=status-1
    staus_array=['confirmed','processed','delivered','rejected']
    return staus_array[status]