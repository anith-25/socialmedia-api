from  django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from .serializers import SignupInputSerializer
from .services import get_tokens_for_user, get_access_token_for_refresh

UserModel = get_user_model()

class SignupAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        input_serializer = SignupInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = input_serializer.save()
        tokens = get_tokens_for_user(user)
        return Response({"message": "Signup Successful", "tokens": tokens})
    

class LoginAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        if not email or not password:
            return Response({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(email=email.lower(), password=password)
        if user:
            tokens = get_tokens_for_user(user)
            return Response({"message": "Login Successful", "tokens": tokens})
        return Response({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)



class RefreshTokenAPIView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        refresh_token = request.data.get("refresh")
        if refresh_token:
            new_access_token = get_access_token_for_refresh(refresh_token)
            return Response({"access": new_access_token})
        else:
            return Response({"message": "Invalid Refresh Token"}, status=status.HTTP_400_BAD_REQUEST)