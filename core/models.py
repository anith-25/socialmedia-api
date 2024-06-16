from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class FriendRequest(models.Model):
    sender = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name="sent_friend_requests")
    receiver = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name="received_friend_requests")
    accepted = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    sent_at = models.DateTimeField(auto_now_add=True)