from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models import User


class UserSerializer(ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'role',]


