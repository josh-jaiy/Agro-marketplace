# Register your models here.
from django.contrib import admin
from .models import User, Seller, Buyer, Product, Transaction

admin.site.register(User)
admin.site.register(Seller)
admin.site.register(Buyer)
admin.site.register(Product)
admin.site.register(Transaction)
