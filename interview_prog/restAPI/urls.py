from .views import *
from django.urls import path, include
from rest_framework.routers import DefaultRouter


api_router = DefaultRouter()

api_router.register(r'products', product_view)
api_router.register(r'categories', category_view)
api_router.register(r'users', user_view)


urlpatterns = [
    path('v1/', include(api_router.urls), name="product"),
    path('v1/api-token-auth/', ObtainAuthToken.as_view(), name='api-token-auth'),
]