import logging

from django.contrib.auth.models import User
from rest_framework import status, request
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate

from django.core.exceptions import ValidationError, ObjectDoesNotExist

from backend.core.base_manager import BaseManager
from backend.user.serializers.user_json import UserJson

logger = logging.getLogger(__name__)


class UserService(BaseManager):
    def __init__(self):
        try:
            super().__init__(model=User)
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex

    def get_by_username(
            self,
            username: str,
            password: str,
    ) -> [UserJson, None]:
        try:
            if username is None:
                raise ValidationError('username is empty')

            if password is None:
                raise ValidationError('password is empty')

            # Use authenticate() to check the user's credentials
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User exists with the provided credentials
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})

            else:
                # Invalid credentials or user does not exist
                return Response(
                    status=400,
                    data={'error': 'Invalid credentials'}
                )

        except ObjectDoesNotExist:
            return None
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex
