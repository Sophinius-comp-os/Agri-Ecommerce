from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    PasswordResetView,
    PasswordResetConfirmView,
)

from .views import (
    UserViewSet,
    ProductViewSet,
    CategoryViewSet,
    OrderViewSet,
    OrderItemViewSet,
    AddressViewSet,
    PaymentViewSet,
)
from rest_framework_simplejwt.views import PasswordResetView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'payments', PaymentViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/password/reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/password/reset/confirm/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]

