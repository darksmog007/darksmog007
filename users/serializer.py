import os
from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    age = serializers.CharField(max_length=200)
    address = serializers.CharField(max_length=200)
    username = serializers.CharField(max_length=200)

    class Meta:
        fields = "__all__"
