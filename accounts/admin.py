from django.contrib import admin

from .models import Customer, Employee, Food, Category, CheckOut, Coupon

# Register your models here.
admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(Food)
admin.site.register(Category)
admin.site.register(Coupon)
admin.site.register(CheckOut)
