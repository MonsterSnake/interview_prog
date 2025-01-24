# from .views import index
from django.urls import path
from .views import index
urlpatterns = [
    path('', index, name=""),
]