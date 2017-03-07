from django.db import models
from .customer import Customer
from .product_type import ProductType


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
    quantity = models.IntegerField()
    description = models.TextField(max_length=300, default='')
    product_type = models.ForeignKey(ProductType, related_name="products",
                                     on_delete=models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customer, related_name="products", on_delete=models.CASCADE)

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
