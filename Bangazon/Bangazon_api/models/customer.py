from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)

    def __str__(self):
        """
        """
        return '{}'.format(self.user.username)

    class Meta:
        """
        """
        verbose_name_plural = "Customers"
