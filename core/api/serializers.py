from django.contrib.auth import get_user_model
from rest_framework import serializers
from ..models import FriendRequest

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id", "name", "email"]

class ReceivedFriendRequestsSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    
    class Meta:
        model = FriendRequest
        fields = ["id", "sender", "accepted"]