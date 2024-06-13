from django.conf import settings
from django.http import Http404
from rest_framework_simplejwt.authentication import JWTAuthentication
from books.models.user import Author


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token[settings.SIMPLE_JWT['USER_ID_CLAIM']]
        try:
            user = Author.objects.get(id=user_id)
        except Author.DoesNotExist:
            raise Http404
        return user