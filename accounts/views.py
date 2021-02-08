from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import datetime
import pytz

from .serializers import (
    CustomerRegistrationSerializer, LoginSerializer, UserSerializer, FoodSerializer, CouponSerializer, CheckoutSerializer, CustomerSerializer, CategorySerializer
)
from .models import Customer, Employee, Food, Category, Coupon, CheckOut

# Create your views here.


class UserList(GenericAPIView):
    '''
        Retrieves specific user
    '''

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            user_id = request.data["id"]
            user = User.objects.get(id=user_id)
        except:
            user = None

        if user is None:
            return JsonResponse({"Error": "User doesn't exist!"}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({"user": UserSerializer(user, context=self.get_serializer_context()).data}, status=status.HTTP_200_OK)


class CustomerUserCreate(GenericAPIView):
    '''
        Registers new user
    '''

    serializer_class = CustomerRegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return JsonResponse({
            "user": UserSerializer(user, context=self.get_serializer_context()).data
        }, safe=False, status=status.HTTP_201_CREATED)


class UserLogin(GenericAPIView):
    '''
        Login registered user
    '''

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        user = authenticate(
            request, username=request.data["username"], password=request.data["password"])
        if user is not None:
            login(request, user)
        else:
            return JsonResponse({"message": "Failed to login"}, status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse({"user": UserSerializer(user, context=self.get_serializer_context()).data}, status=status.HTTP_200_OK)


class CustomerUser(GenericAPIView):
    '''
        Verifies if the user is customer
    '''

    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.data["user_id"]

        try:
            user = Customer.objects.get(user_id=user_id)
        except:
            user = None

        if user is None:
            return JsonResponse({"Customer": False}, status=status.HTTP_404_NOT_FOUND)

        return JsonResponse({"Customer": True}, status=status.HTTP_200_OK)


class FoodList(GenericAPIView):
    '''
        Retrieves food menu
    '''

    serializer_class = FoodSerializer

    def get(self, request, *args, **kwargs):
        foods = Food.objects.all()
        data = {}
        for food in foods:
            if food.category.name == "Pizza":
                data.update({
                    f"{food.id}": {
                        "name": food.name,
                        "image": str(food.photo),
                        "price": food.price,
                        "size": food.size,
                        "preparation_time": food.preparation_time,
                        "category": food.category.name
                    }
                })
            else:
                data.update({
                    f"{food.id}": {
                        "name": food.name,
                        "image": str(food.photo),
                        "price": food.price,
                        "preparation_time": food.preparation_time,
                        "category": food.category.name
                    }
                })

        return JsonResponse(data, status=status.HTTP_200_OK)


class CouponList(GenericAPIView):
    '''
        Validates discount coupon
    '''

    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        now = datetime.datetime.utcnow()
        now = pytz.utc.localize(now)

        name = request.data["name"]
        try:
            coupon = Coupon.objects.get(name=name)
        except:
            return JsonResponse({"message": "Coupon does not exist"}, status=status.HTTP_404_NOT_FOUND)

        if (now.date()-coupon.created_at.date()).days > coupon.duration.days:
            if coupon.active:
                coupon.active = False
                coupon.save()
        data = {
            "name": coupon.name,
            "percentage": coupon.percentage,
            "duration": coupon.duration.days,
            "status": coupon.active,
            "created_at": coupon.created_at
        }

        return JsonResponse(data, status=status.HTTP_200_OK)


class CheckoutList(GenericAPIView):
    '''
        Checkout the card of user
    '''

    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data["user"]
        item_id = request.data["items"]

        total = request.data["total"]
        address = request.data["address"]

        items = []

        try:
            for item in item_id:
                items.append(Food.objects.get(id=item))

            user = Customer.objects.get(id=user_id)

            order = CheckOut.objects.create(
                user=user,
                total=total,
                address=address
            )
            order.items.set(items)
            order.save()

            return JsonResponse({"order": f"Order Success, #{order.number}!"}, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"order": "Order Failed!"}, status=status.HTTP_400_BAD_REQUEST)


class CheckoutUser(GenericAPIView):
    '''
        Retrieves all the checkouts of user
    '''

    serializer_class = CheckoutSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_id = request.data["user_id"]

        try:
            user = Customer.objects.get(user_id=user_id)
        except:
            user = None

        if user is None:
            return JsonResponse({"Error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

        checkouts = CheckOut.objects.filter(user=user)
        data = {}

        for checkout in checkouts:
            items_list = []
            for item in checkout.items.values():
                items_list.append(item)

            data.update({
                f"{checkout.user.user.username}": {
                    "number": checkout.number,
                    "total": checkout.total,
                    "items": items_list,
                    "address": checkout.address,
                    "ordered_at": checkout.ordered_at
                }
            })

        return JsonResponse(data, status=status.HTTP_200_OK)


class CategoryList(GenericAPIView):
    '''
        Retrieves categories
    '''

    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        data = {}
        serial = 0

        for category in categories:
            data.update({
                f"{serial}": {
                    "id": category.pk,
                    "name": category.name
                }
            })

            serial += 1

        return JsonResponse(data, status=status.HTTP_200_OK)
