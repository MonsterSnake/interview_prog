from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class category_serializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = '__all__'


class products_serializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'


class user_serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

