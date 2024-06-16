from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status

from ..models import FriendRequest
from .serializers import UserSerializer, ReceivedFriendRequestsSerializer

UserModel = get_user_model()

class SearchUserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        search = request.GET.get("search")
        user = request.user
        if not search:
            return Response({"message": "No search parameter"}, status=status.HTTP_400_BAD_REQUEST)
        search = search.strip()
        exact_match_user = UserModel.objects.filter(email__iexact=search).exclude(pk=user.id).first()
        if exact_match_user:
            serializer = UserSerializer(exact_match_user)
            return Response(serializer.data)
        users = UserModel.objects.filter(name__icontains=search).exclude(pk=user.id).all()
        pagination = PageNumberPagination()
        pagination.page_size = 10
        page_obj = pagination.paginate_queryset(users, request)
        serializer = UserSerializer(page_obj, many=True)
        return Response(serializer.data)
    
class FriendsListView(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        serializer = UserSerializer(user.friends.all(), many=True)
        return Response(serializer.data)
    
class SendFriendRequestAPIView(APIView):
    def post(self, request, *args, **kwargs):
        receiver_id = request.data.get("receiver")
        user = request.user
        receiver = get_object_or_404(UserModel, pk=receiver_id)
        if user == receiver:
            return Response({"message": "You cannot send a friend request to yourself."}, status=status.HTTP_400_BAD_REQUEST)
        time_before_1_mins = datetime.now() - timedelta(minutes=1)
        if receiver in user.friends.all():
             return Response({"message": "You are already friends."}, status=status.HTTP_400_BAD_REQUEST)
        elif FriendRequest.objects.filter(sender=user, receiver=receiver).exists() or FriendRequest.objects.filter(sender=receiver, receiver=user).exists():
            return Response({"message": "There is already a pending friend request."}, status=status.HTTP_400_BAD_REQUEST)
        elif FriendRequest.objects.filter(sender=user, sent_at__gte=time_before_1_mins).count() >= 3:
            return Response({"message": "Friend Request limit exceeded, please try after some time."}, status=status.HTTP_400_BAD_REQUEST)
        FriendRequest.objects.create(sender=user, receiver=receiver)
        return Response({"message": "Friend request successfully sent"})
    

class AcceptFriendRequestAPIView(APIView):
    def post(self, request, pk, *args, **kwargs):
        friend_request = get_object_or_404(FriendRequest, pk=pk)
        friend_request.sender.friends.add(friend_request.receiver)
        friend_request.accepted = True
        friend_request.save()
        return Response({"message": "Friend request successfully accepted."})
    
class RejectFriendRequestAPIView(APIView):
    def post(self, request, pk, *args, **kwargs):
        friend_request = get_object_or_404(FriendRequest, pk=pk)
        friend_request.delete()
        return Response({"message": "Friend request successfully rejected."})


class PendingFriendRequestsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        friend_requests = FriendRequest.objects.filter(receiver=request.user, accepted=False)
        serializer = ReceivedFriendRequestsSerializer(friend_requests, many=True)
        return Response(serializer.data)