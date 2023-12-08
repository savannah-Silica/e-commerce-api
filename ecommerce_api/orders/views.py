from django.shortcuts import render, redirect
from .models import OrderStatus, Order
from .forms import OrderStatusForm, OrderForm


#############################################################################################################################
#                                                   views for the OrderStatus model                                         #
#############################################################################################################################

# view that returns a list of all order statuses
def order_status_list(request):
    statuses = OrderStatus.objects.all()
    return render(request, 'orders/order_status_list.html', {'statuses': statuses})

# view that allows the creation of a new order status
def order_status_create(request):
    form = OrderStatusForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('order_status_list')
    return render(request, 'orders/order_status_form.html', {'form': form})

# view that allows the updating of an existing order status
def order_status_update(request, pk):
    status = OrderStatus.objects.get(pk=pk)
    form = OrderStatusForm(request.POST or None, instance=status)
    if form.is_valid():
        form.save()
        return redirect('order_status_list')
    return render(request, 'orders/order_status_form.html', {'form': form})

# view that allows the deletion of an existing order status
def order_status_delete(request, pk):
    OrderStatus.objects.get(pk=pk).delete()
    return redirect('order_status_list')


#############################################################################################################################
#                                                   views for the Order model                                               #
#############################################################################################################################
# view that allow to create a new order
def order_create(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm()
    return render(request, 'orders/order_form.html', {'form': form})

# view that list all orders
def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

# view that allow to update an existing order
def order_update(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)
    return render(request, 'orders/order_form.html', {'form': form})

#view that allow to delete an existing order
def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'orders/order_confirm_delete.html', {'order': order})