from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('audit', views.DetailedAccountViewSet, basename='audit')
router.register('account', views.AccountViewSet,basename='account')
router.register('cart', views.CartViewSet,basename='cart')
router.register('addresses', views.AddressViewSet,basename='addresses')
router.register('products', views.ProductViewSet,basename='product')
router.register('orders', views.OrderViewSet,basename='orders')


urlpatterns = [
    path('',include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'), 
]