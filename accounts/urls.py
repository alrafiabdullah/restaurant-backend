from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('user', views.UserList.as_view(), name='user'),
    path('register', views.CustomerUserCreate.as_view(), name='register'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('food', views.FoodList.as_view(), name='food'),
    path('coupon', views.CouponList.as_view(), name='coupon'),
    path('checkout', views.CheckoutList.as_view(), name='checkout'),
    path('checkout/user', views.CheckoutUser.as_view(), name='checkout-user'),
    path('customer', views.CustomerUser.as_view(), name='customer'),
    path('category', views.CategoryList.as_view(), name='category'),

    path('token', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
