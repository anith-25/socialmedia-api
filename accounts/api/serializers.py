from rest_framework import serializers
from accounts.models import MyUser
from .exceptions import MailAlreadyInUseException


class SignupInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8)

    def validate(self, attrs):
        email = attrs.get("email")
        if email and MyUser.objects.filter(email__iexact=email.lower()).exists():
            raise MailAlreadyInUseException
        return attrs

    def create(self, validated_data):
        name = validated_data.get("name")
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = MyUser.objects.create(email=email.lower(), name=name)
        user.set_password(password)
        user.save()
        return user