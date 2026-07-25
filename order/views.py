from django.shortcuts import redirect
from django.contrib import messages
from .models import Order

def save_order(request):
    if request.method == "POST":

        Order.objects.create(
            customer_name=request.POST["name"],
            phone=request.POST["phone"],
            menu_item=request.POST["food"],
            quantity=request.POST["quantity"],
            address=request.POST["address"],
        )

        messages.success(request, "Your order has been placed successfully!")

    return redirect("/")