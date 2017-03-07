from django.db import models
from .payment_type import PaymentType
from .product import Product
from .customer import Customer


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

    customer = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE)
    completed = models.IntegerField(default=0)
    payment_type = models.ForeignKey(PaymentType, null=True, on_delete=models.CASCADE)
    product = models.ManyToManyField(Product, through='OrderProduct')

    def __str__(self):
        """
        Method to create a string representing a Order of a particular Customer of Bangazon API
        """
        return '{}'.format(self.completed)

    class Meta:
        """
        Class defining metadata for results of querying the Order table of
            Bangazon API
        """
        verbose_name_plural = "Orders"


class OrderProduct(models.Model):
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
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, mull=True, on_delete=models.CASCADE)

    def __str__(self):
        """
        Method to create a string representing a ProductOrder sold by a
            particular User(seller) of Bangazon API
        """
        return str(self.id)

    class Meta:
        """
        Class defining metadata for results of querying the Product/Order
            table of Bangazon API
        """
        ordering = ('order',)
