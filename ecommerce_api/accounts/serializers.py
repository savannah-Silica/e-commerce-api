from typing import Any, Dict
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.settings import api_settings
from django.contrib.auth.models  import update_last_login
from django.conf import settings

class CustomUserSerializers(serializers.ModelSerializer):
    created=serializers.DateTimeField(read_only=True)
    updated=serializers.DateTimeField(read_only=True)

    class Meta:
        model=CustomUser
        fields=[
            "id","email","is_active","created","updated"
        ]
        read_only_field=['is_active']

class RegisterSerializer(CustomUserSerializers):
    """
    Registration Serializer for request and user creation
    """
    password=serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model=CustomUser
        fields=["id","email","password"]

    
    def create(self,validated_data):
        return CustomUser.objects.create_user(**validated_data)

class LoginSerializers(TokenObtainPairSerializer):
    user = CustomUserSerializers(read_only=True)  

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)

        user_serializer = CustomUserSerializers(instance=self.user)  
        data['user'] = user_serializer.data  

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

  
        if getattr(settings, 'UPDATE_LAST_LOGIN', False):
            update_last_login(self.context.get('request'), self.user)

        return data

