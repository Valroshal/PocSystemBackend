from typing import Union

from django.db.models import Q, QuerySet
from rest_framework.exceptions import ValidationError

from backend.core.base_model import BaseModel


class BaseManager(object):

    def __init__(
            self,
            model: type(BaseModel)
    ):
        try:
            self.model: type(BaseModel) = model
        except Exception as ex:
            raise ex

    def get_by_id(
            self,
            model_id,
    ) -> Union[type(BaseModel), None]:
        try:
            if not model_id:
                raise ValidationError('model_id are empty')

            result = self.model.objects.filter(pk=model_id).last()

            if not result:
                return None

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def get(
            self,
            filters: Q,
            include_deleted: bool = False
    ) -> QuerySet[type(BaseModel)]:
        try:
            if filters is None:
                raise ValidationError('filters empty')
            if not include_deleted:
                filters = Q(filters, is_deleted=False)

            result = self.model.objects.filter(filters)

            return result

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    # def get_value_list(
    #         self,
    #         filters: Q,
    #         value: str,
    #         include_deleted: bool = False
    # ) -> QuerySet:
    #     try:
    #         if not filters:
    #             raise ValidationError('filters empty')
    #         if not value:
    #             raise ValidationError('value empty')
    #         if not include_deleted:
    #             filters = Q(filters, is_deleted=False)
    #
    #         result = self.model.objects.filter(filters).values_list(value, flat=True)
    #
    #         return result
    #
    #     except ValidationError as ex:
    #         raise ex
    #     except Exception as ex:
    #         raise ex

    def create(
            self,
            **kwargs
    ) -> type(BaseModel):
        try:
            if not kwargs:
                raise ValidationError('kwargs empty')

            model = self.model.objects.create(**kwargs)

            return model

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def update(
            self,
            model_id: any,
            **kwargs
    ) -> type(BaseModel):
        try:
            if not model_id:
                raise ValidationError('model_id empty')
            if not kwargs:
                raise ValidationError('kwargs empty')

            self.model.objects.filter(pk=model_id).update(**kwargs)
            model = self.model.objects.filter(pk=model_id).last()

            return model

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

    def delete(
            self,
            model_id: any,
    ):
        try:
            if not model_id:
                raise ValidationError('model_id empty')

            delete_obj = self.model.objects.filter(pk=model_id).last()
            delete_obj.is_deleted = True
            delete_obj.save()

        except ValidationError as ex:
            raise ex
        except Exception as ex:
            raise ex

