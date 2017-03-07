from django.db import models


class ProductType(models.Model):
    """
    Class to create a table representing a Product Category of Bangazon API
    Extension of models.Model

    Variables:
        name: the Product Category's name

    Authors: Julia Kim-Chung, Jack Pinkston, Sam Phillips, Drew Martin,
        Ben Marks
    """
    created = models.DateTimeField(auto_now_add=True)
    label = models.CharField(max_length=50, blank=True, unique=True)

    def __str__(self):
        """
        Method to create a string representing a Product Category of
            Bangazon API
        """
        return self.label

    class Meta:
        """
        Class defining metadata for results of querying the Product Category
            table of Bangazon API
        """
        ordering = ('-created',)
