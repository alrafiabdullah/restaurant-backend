from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from .models import Customer, Food, Coupon, CheckOut, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class CustomerRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "confirm_password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        if validated_data["password"] != validated_data["confirm_password"]:
            raise serializers.ValidationError(
                {"password": "passwords don't match!"})

        user = User.objects.create_user(
            validated_data["username"], validated_data["email"], validated_data["password"],)
        Customer.objects.create(user=user)

        return user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password",)
        extra_kwargs = {"password": {"write_only": True}}


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"


class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = "__all__"


class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckOut
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
