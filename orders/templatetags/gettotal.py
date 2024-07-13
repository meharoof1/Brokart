from django import template

register=template.Library() # To register
@register.simple_tag(name='gettotal') # Add as decorator , name='gettotal' is the name should load in the template 
def gettotal(cart):  # is to pass cart item
    total=0
    for item in cart.added_items.all(): # this is to get all the cart items
        total+=item.quantity*item.product.price
    return total