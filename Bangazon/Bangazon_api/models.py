from django.db import models

class User(models.Model):
    """
    Class to represent a user on Bangazon
    """
    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    date_of_birth = models.DateField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        ordering = ('last_name',)



class PaymentMethod(models.Model):
    """
    Class to represent a payment method for a user on Bangazon
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    account_number = models.CharField(max_length=100, blank=True, default='')
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class Order(models.Model):
    """
    Class to represent an order on Bangazon
    """
    active = models.BooleanField(default=False)
    payment_method_id = models.ForeignKey("PaymentMethod", on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ('user_id',)



class ProductCategory(models.Model):
    """
    Class to represent a category of products on Bangazon
    """      
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class Product(models.Model):
    """
    Class to represent a product for sale on Bangazon
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity_available = models.IntegerField()
    description = models.TextField(max_length=300, default='')
    product_category_id = models.ForeignKey("ProductCategory", on_delete=models.CASCADE)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)



class ProductOrder(models.Model):
    """
    Class to represent a product for an order on Bangazon
    """
    product_id = models.ForeignKey("Product", on_delete=models.CASCADE)
    order_id = models.ForeignKey("Order", on_delete=models.CASCADE)

    class Meta:
        ordering = ('order_id',)
