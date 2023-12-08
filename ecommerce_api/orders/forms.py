from django import forms
from .models import OrderStatus, Order

# form that allow CRUD operations on OrderStatus model
class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = OrderStatus
        fields = '__all__'
        

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__' 