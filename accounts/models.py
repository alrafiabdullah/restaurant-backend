from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

import datetime
import string
# Create your models here.

User._meta.get_field('email')._unique = True


def random_string():
    length = 6
    return get_random_string(length=length, allowed_chars=string.ascii_uppercase+string.digits)


def order_number():
    length = 15
    return get_random_string(length=length, allowed_chars=string.ascii_lowercase+string.digits)


class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# imagecdn.dev
class Food(models.Model):
    DEFAULT = 0
    SHORT = 6
    MEDIUM = 8
    LARGE = 12

    SIZE_CHOICES = (
        (SHORT, 6), (MEDIUM, 8), (LARGE, 12), (DEFAULT, 0)
    )

    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="foods/")
    price = models.PositiveIntegerField(default=0)
    preparation_time = models.PositiveIntegerField(default=0)
    size = models.PositiveIntegerField(
        choices=SIZE_CHOICES, null=True, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class CheckOut(models.Model):
    number = models.CharField(
        max_length=500, unique=True, default=order_number)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total = models.PositiveIntegerField(default=0)
    items = models.ManyToManyField(Food, blank=False)
    address = models.TextField(blank=False, max_length=1000)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number


class Coupon(models.Model):
    SHORT = datetime.timedelta(days=1)
    MEDIUM = datetime.timedelta(days=3)
    LONG = datetime.timedelta(days=5)
    WEEK = datetime.timedelta(days=7)
    HALF = datetime.timedelta(days=15)
    MONTH = datetime.timedelta(days=30)

    DURATION_CHOICES = (
        (SHORT, '1 day'), (MEDIUM, '3 days'), (LONG, '5 days'),
        (WEEK, '7 days'), (HALF, '15 days'), (MONTH, '30 days'),
    )

    name = models.CharField(max_length=100, unique=True, default=random_string)
    percentage = models.PositiveIntegerField(default=0)
    duration = models.DurationField(choices=DURATION_CHOICES, default=SHORT)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
