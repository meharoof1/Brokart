from django.shortcuts import render,redirect
from .models import Order,OrderedItem
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='account')
def show_cart(request):
    user=request.user
    customer=user.customer_profile
    cart_obj,created=Order.objects.get_or_create(
        owner=customer,
        order_status=Order.CART_STAGE
    )
    context={'cart':cart_obj}
    return render(request,'cart.html',context)

@login_required(login_url='account')
def remove_item_from_cart(request,pk):
    item=OrderedItem.objects.get(pk=pk)
    if item:
        item.delete()
    return redirect('cart')

@login_required(login_url='account')
def add_to_cart(request):
    if request.POST:
        user=request.user
        customer=user.customer_profile
        quantity=int(request.POST.get('quantity'))
        product_id=request.POST.get('product_id')
        cart_obj,created=Order.objects.get_or_create(
            owner=customer,
            order_status=Order.CART_STAGE
        )
        product=Product.objects.get(pk=product_id)
        Ordered_item,created=OrderedItem.objects.get_or_create(
            product=product,
            owner=cart_obj
        )
        if created:
            Ordered_item.quantity=quantity
            Ordered_item.save()
        else:
            Ordered_item.quantity= Ordered_item.quantity+quantity
            Ordered_item.save()
    return redirect('cart')

@login_required(login_url='account')
def checkout_cart(request):
    if request.POST:
        try:
            user=request.user
            customer=user.customer_profile
            total=float(request.POST.get('total'))
            order_obj=Order.objects.get(
                owner=customer,
                order_status=Order.CART_STAGE
            )
            if order_obj:
                order_obj.order_status=Order.ORDER_CONFIRMED
                order_obj.total_price=total
                order_obj.save()
                status_message="Your order is processed. will be delivered in 2 days"
                messages.success(request,status_message)
            else:
                status_message="unable to process. your cart is empty"
                messages.error(request,status_message)
        except Exception as e:
            status_message="unable to process. your cart is empty"
            messages.error(request,status_message)
    return redirect('cart')


@login_required(login_url='account')
def show_orders(request):
    user=request.user
    customer=user.customer_profile
    all_orders=Order.objects.filter(owner=customer).exclude(order_status=Order.CART_STAGE)
    context={'orders':all_orders}
    return render(request,'orders.html',context)



@login_required(login_url='account')
def view_orders(request):
    user=request.user
    customer=user.customer_profile
