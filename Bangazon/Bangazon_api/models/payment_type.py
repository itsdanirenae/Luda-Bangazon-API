from django.db import models
from .customer import Customer


class PaymentType(models.Model):
    """
    Class to create a table representing a Payment Method, tied to a
    particular Customer of Bangazon API
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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=50, default='')
    created = models.DateTimeField(auto_now_add=True)
    account_number = models.CharField(max_length=16, unique=True, default='')
    ccv = models.CharField(max_length=3)
    expiration_date = models.CharField(max_length=10)

    def __str__(self):
        """
        Method to create a string representing a Payment Method of a
            particular User(customer) of Bangazon API

        Returns a string representaion of the payment method's name field
        """
        return '{} {}'.format(self.payment_type, self.account_number)

    class Meta:
        """
        Class defining metadata for results of querying the Payment Method
            table of Bangazon API
        """
        verbose_name_plural = 'PaymentTypes'
