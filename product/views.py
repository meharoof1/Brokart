from django.shortcuts import render
from . models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    featured_products=Product.objects.order_by('priority')[:4]
    latest_products=Product.objects.order_by('-id')[:3]
    context={
        'featured_products':featured_products,
        'latest_products':latest_products
    }
    return render (request,'index.html',context)

def list_products(request):
    page=1
    if request.GET:
        page=request.GET.get('page',1)
    product_list=Product.objects.all()
    product_page=Paginator(product_list,10)
    product_list=product_page.get_page(page)
    context={'product':product_list}
    return render (request,'products.html',context)


def detail_products(request,pk):
    product=Product.objects.get(pk=pk)
    context={'product':product}
    return render (request,'products_detail.html',context)



def search_products(request):
    query = request.GET.get('q', '').strip()
    products = Product.objects.none()  
    error_message = None

    if query:
        products = Product.objects.filter(title__icontains=query)
        if not products.exists():
            error_message = "No products match your search criteria."
    else:
        error_message = "Please enter a search term."


    paginator = Paginator(products, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'search_results.html', {
        'products': page_obj,
        'query': query,
        'error_message': error_message,
    })