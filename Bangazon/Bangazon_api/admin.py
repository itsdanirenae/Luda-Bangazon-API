from django.contrib import admin
from .models.product import Product
from .models.order import Order
from .models.order import OrderProduct
from .models.payment_type import PaymentType
from .models.product_type import ProductType
from .models.customer import Customer


# Register your models here.
admin.site.register(Product)
admin.site.register(OrderProduct)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(ProductType)
admin.site.register(Customer)
