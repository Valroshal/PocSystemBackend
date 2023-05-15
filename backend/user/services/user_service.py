import logging

from django.contrib.auth.models import User
from rest_framework import status, request
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
                raise ValidationError('email is empty')

            if password is None:
                raise ValidationError('password is empty')

            # Use authenticate() to check the user's credentials
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # User exists with the provided credentials
                # Perform additional actions or redirect to a success page
                return Response(
                    status=status.HTTP_200_OK
                )
            else:
                # Invalid credentials or user does not exist
                return Response(
                    status=status.HTTP_204_NO_CONTENT
                )

        except ObjectDoesNotExist:
            return None
        except Exception as ex:
            logger.error(str(ex), exc_info=True)
            raise ex
