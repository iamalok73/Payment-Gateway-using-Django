from django.shortcuts import render
from .forms import CoffeePaymentForm

import razorpay


from .models import ColdCoffee
# Create your views here.




def coffee_payment(request):
    if request.method == "POST":
        name = request.POST.get("name")
        amount = int(request.POST.get("amount"))*100
        
        # create razorpay client 
        
        
        client = razorpay.Client(auth=(""))
        
        response_payment = razorpay.Order.create(dict(amount = amount,currency ="INR"))
        
        # print(response_payment)
        
        order_id = response_payment['id']
        order_status = response_payment['status']
        
        if order_status =="created":
            cold_coffee = ColdCoffee(
                name = name,
                amount = amount,
                order_id = order_id,
            )
            cold_coffee.save()
            form = CoffeePaymentForm(request.POST or None)
            return render(request, "coffee_paytment.html", {"form" :form })
    form = CoffeePaymentForm()
    return render(request, "coffee_paytment.html", {'form':form})