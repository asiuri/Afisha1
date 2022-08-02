import json

from rest_framework import serializers
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.exceptions import ValidationError
from validate_email import validate_email

class AuthValidateSerializers(serializers.Serializer):
    username=serializers.CharField(min_length=5,max_length=100)
    password=serializers.CharField(max_length=7)

class RegistrationValidateSerializer(serializers.Serializer):
    username=serializers.CharField()
    password = serializers.CharField()
    email=serializers.EmailField(required=True)

    def validate_username(self, username):
        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('User already exists')
        return username

    def post(self,request):
        data=json.loads(request.body)
        email=data['email']
        if not validate_email(email):
            return JsonResponse({'email error':'Email is invalid' },status=400)
        if User.objects.filter(email=email).exist():
            return JsonResponse({'email error':'Sorry email is use,choose another one'},status=409)
        return JsonResponse()