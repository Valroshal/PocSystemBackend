from django.db import models

from backend.core.base_model import BaseModel


class Product(BaseModel):
    id = models.CharField(primary_key=True, default='', max_length=64)

    name = models.CharField(
        blank=False,
        null=False,
        max_length=64
    )

    description = models.CharField(
        blank=False,
        null=False,
        max_length=258
    )

    price = models.DecimalField(
        blank=False,
        null=False,
        max_digits=8,
        decimal_places=2
    )

    quantity = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )

    favorite = models.BooleanField(
        blank=False,
        null=False,
        default=False
    )


