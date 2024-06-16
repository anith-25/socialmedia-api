from django.urls import path
from .views import LoginAPIView, SignupAPIView, RefreshTokenAPIView

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="login"),
    path("signup/", SignupAPIView.as_view(), name="signup"),
    path("token/refresh/", RefreshTokenAPIView.as_view(), name="refresh_token")
]
