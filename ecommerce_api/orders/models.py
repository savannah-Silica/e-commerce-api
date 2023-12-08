from django.db import models

# model that represents all possible order statuses
class OrderStatus(models.Model):
    # abbreviated name for the status
    abbreviation = models.CharField(max_length=4, null=True, blank=True)
    # description of the status
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.name

# model that represents a single order, including status of the order, date it was created and updated, total price and the customer who placed the order
# this model should be later updated to include a ForeignKey to the Customer model and total price should be calculated based on the items in the order
class Order(models.Model):
    # the status of the order
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE, null=True, blank=True)
    # the date the order was created
    created_at = models.DateTimeField(auto_now_add=True)
    # the date the order was last updated
    updated_at = models.DateTimeField(auto_now=True)
    # the total price of the order
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # the customer who placed the order - temporarily set as CharField but should later be changed to a ForeignKey to the Customer model as shown in the commented out line below
    # customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE, null=True, blank=True)
    customer = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.id)