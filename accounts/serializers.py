from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser

class CustomUserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        ]

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data["password"])
        return super(CustomUserSerializer, self).create(validated_data)
    
    def update(self, instance, validated_data):
        if validated_data.get("password", None) != None:
            validated_data["password"] = make_password(validated_data["password"])
        return super().update(instance, validated_data)
    

class MyTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        return token