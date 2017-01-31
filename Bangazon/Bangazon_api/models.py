from django.db import models
from django.contrib.auth.models import User


class PaymentMethod(models.Model):
    """
    Class to create a table representing a Payment Method, tied to a
    particular User(customer) of Bangazon API
    Extension of models.Model

    Variables:
        created: the current local date and time of creation
        name: the payment method's name
        account_number: the payment method's unique identifier
        customer: the foreign key of the user, related_name is for the
            PaymentMethod model: related_name should be lowercase,
            pluralized model name

    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
        Ben Marks
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, default='')
    account_number = models.CharField(max_length=100, blank=True, default='')
    customer = models.ForeignKey(User, related_name="payment_methods",
        on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Payment Method
            table of Bangazon API
        """
        ordering = ('name',)


class Order(models.Model):
    """
    Class to create a table representing an Order, tied to a
        particular User(customer) of Bangazon API
    Extension of models.Model

    Variables:
        active: A boolean denoting whether the order is being processed
        created: the current local date and time of creation
        payment_method: the foreign key of the user's payment method, only
            needed when the order is "active", related_name is for the Order
            model; related_name should be lowercase, pluralized model name

        customer: the foreign key of the User(customer)related_name is for
        the Order model; related_name should be lowercase, pluralized model
        name

    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
        Ben Marks
    """
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    payment_method = models.ForeignKey("PaymentMethod",
        related_name="orders", on_delete=models.CASCADE)
    customer = models.ForeignKey(User, related_name="orders",
        on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Order of a particular User
            (customer) of Bangazon API
        """
        return str(self.id)

    class Meta:
        """
        Class defining metadata for results of querying the Order table of
            Bangazon API
        """
        ordering = ('customer',)


class ProductCategory(models.Model):
    """
    Class to create a table representing a Product Category of Bangazon API
    Extension of models.Model

    Variables:
        name: the Product Category's name

    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
        Ben Marks
    """
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        """
        Method to create a string representing a Product Category of
            Bangazon API
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Product Category
            table of Bangazon API
        """
        ordering = ('name',)


class Product(models.Model):
    """
    Class to create a table representing a Product, tied to a
        particular User(seller) of Bangazon API
    Extension of models.Model

    Variables:
        created: the local date and time of creation (auto-filled)
        name: the product's name
        price: the price of the product, in US dollars
        quantity_available: the amount available for purchase
        description: a description of the product
        product_category: the foreign key of the product category,
            related_name is for the Product model; related_name should
            be lowercase, pluralized model name
        seller: the foreign key of the User(seller), related_name is for
            the Product model; related_name should be lowercase, pluralized
            model name


    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
        Ben Marks
    """
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, default='')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity_available = models.IntegerField()
    description = models.TextField(max_length=300, default='')
    product_category = models.ForeignKey("ProductCategory",
        related_name="products", on_delete=models.CASCADE)
    seller = models.ForeignKey(User, related_name="products",
        on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a Product sold by a
            particular User(seller) of Bangazon API
        """
        return self.name

    class Meta:
        """
        Class defining metadata for results of querying the Product table of
            Bangazon API
        """
        ordering = ('name',)


class ProductOrder(models.Model):
    """
    Class to create a table representing a Product Order, tying products to a
        particular Order
    Extension of models.Model

    Variables:
        product: foreign key of an added product, related_name is for the
            ProductOrder model; related_name should be lowercase, pluralized
            model name

        order: foreign key of the order, related_name is for the
            ProductOrder model; related_name should be lowercase, pluralized
            model name

    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
    Ben Marks
    """
    product = models.ForeignKey("Product", related_name="product_orders",
        on_delete=models.CASCADE)
    order = models.ForeignKey("Order", related_name="product_orders",
        on_delete=models.CASCADE)

    class Meta:
        """
        Class defining metadata for results of querying the Product/Order
            table of Bangazon API
        """
        ordering = ('order',)
