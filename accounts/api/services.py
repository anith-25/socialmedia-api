from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def get_access_token_for_refresh(refresh):
    refresh_token = RefreshToken(refresh)
    try:
        refresh_token.check_exp()
    except TokenError:
        return TokenError
    access_token = refresh_token.access_token
    return str(access_token)