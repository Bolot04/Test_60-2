from django.shortcuts import render
from polls.models import Order 
from polls.form import OrderForm
from django.http import HttpResponse
# Create your views here.
def home(request):
    if request.method == "GET":
        return render(request, "base.html")
    
def orders_list_view(request):
    orders = Order.objects.all()
    if request.method == "GET":
        return render(request,"orders/order.list.html", context={"orders": orders})
    

def order_create_view(request):
    if request.method == "GET":
        form = OrderForm
        return render(request, "orders/order.create.html", context={"form": form})
    elif request.method == "POST":
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            Order.objects.filter(
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                price = form.cleaned_data["price"]
            )    
        return HttpResponse("Order created")