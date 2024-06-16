from django.urls import path
from .views import SearchUserAPIView, FriendsListView, SendFriendRequestAPIView, AcceptFriendRequestAPIView, RejectFriendRequestAPIView, PendingFriendRequestsAPIView

urlpatterns = [
    path("users/", SearchUserAPIView.as_view(), name="search_users"),
    path("friends/", FriendsListView.as_view(), name="friends_list"),
    path("friendrequest/send/", SendFriendRequestAPIView.as_view(), name="send_friend_request"),
    path("friendrequest/<int:pk>/accept/", AcceptFriendRequestAPIView.as_view(), name="accept_friend_request"),
    path("friendrequest/<int:pk>/reject/", RejectFriendRequestAPIView.as_view(), name="reject_friend_request"),
    path("friendrequest/pending/", PendingFriendRequestsAPIView.as_view(), name="pending_friend_requests"),    
]
