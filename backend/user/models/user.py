from django.contrib.auth import get_user_model
from django.db import models

from backend.core.base_model import BaseModel

AuthUser = get_user_model()


class User(BaseModel):
    id = models.CharField(primary_key=True, default='', max_length=64)
    auth_user = models.OneToOneField(AuthUser, on_delete=models.CASCADE)
    email = models.EmailField(
        blank=False,
        null=False,
    )
