from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializers import AuthValidateSerializers,RegistrationValidateSerializer
from rest_framework.views import APIView



class AuthorizationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer=AuthValidateSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(**serializer.validated_data)#username=admin,password=123
        if user:
           try:
              token=Token.objects.get(user=user)
           except Token.DoesNotExist:
                 token=Token.objects.create(user=user)
           return Response({'key':token.key})
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

# @api_view(['POST'])
# def registration(request):
#     serializer = RegistrationValidateSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user = User.objects.create_user(**serializer.validated_data)
#     return Response(data={
#         'id': user.id,
#         'username': user.username
#     })

class RegistrationAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(**serializer.validated_data)
        return Response(data={
            'id': user.id,
            'username': user.username
        })



class VerifyAPIView(APIView):
    def verify_email(request):
        serializer = RegistrationValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user= User.objects.create_user(**serializer.validated_data)
        return Response(data={
            'id': user.id,
            'email':user.user.email
        })



