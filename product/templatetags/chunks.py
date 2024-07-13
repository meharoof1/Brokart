from django import template

register=template.Library() # To register
@register.filter(name='chunks') # Add as decorator , name='chunks' is the name should load in the template 
def chunks(list_data,chunk_size): # list_data is the list and chunk_size is the number of products should display in one row  
    chunk=[] # is an empty list in which the value is appended
    i=0
    for data in list_data:
        chunk.append(data)
        i=i+1
        if i == chunk_size:
            yield chunk
            chunk=[]
    yield chunk