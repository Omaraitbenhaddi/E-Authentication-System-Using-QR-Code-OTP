from dataclasses import fields
from operator import ge
from pyexpat import model
from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import User, EmailOTP

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['email','password']
class EmailOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailOTP
        fields = ['email','otp']
User =get_user_model()
class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            if User.objects.filter(email=email).exists():
                user = authenticate(request=self.context.get('request'),
                                    email=email, password=password)
                
            else:
                msg = {'detail': 'email number is not registered.',
                       'register': False}
                raise serializers.ValidationError(msg)

            if not user:
                msg = {
                    'detail': 'Unable to log in with provided credentials.', 'register': True}
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
