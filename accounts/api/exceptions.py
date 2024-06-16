from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.exceptions import APIException


class MailAlreadyInUseException(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_code = _("email_exists")
    default_detail = _("The email is already in use.")