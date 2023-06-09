from django.http import HttpResponse
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from rest_framework import status, renderers
from rest_framework.response import Response
from django.contrib.auth import authenticate

from backend.product.services.product_service import ProductService
from backend.user.services.user_service import UserService


# Create your views here.
class ProductApi(APIView):
    renderer_classes = [renderers.JSONRenderer]

    def post(self, request):
        try:
            pr_id = request.data.get('pr_id')
            name = request.data.get('name')
            description = request.data.get('description')
            price = request.data.get('price')
            quantity = request.data.get('quantity')
            favorite = request.data.get('favorite')
            ProductService().create()

            print('successfully created')
            return Response(
                status=status.HTTP_200_OK
            )


        except ValidationError as ex:
            print('error', ex)
            return Response(
                data=str(ex),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as ex:
            print('error', ex)
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def put(self, request):
        try:

            ProductService().update_favorite(
                product_id=request.data.get('id'),
                favorite=request.data.get('favorite'),
            )

            return Response(
                status=status.HTTP_200_OK
            )

        except ValidationError as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def get(self, request):
        try:

            products = ProductService().get_all()

            if products is None:
                return Response(
                    data=[],
                    status=status.HTTP_204_NO_CONTENT
                )

            return Response(
                data=products,
                status=status.HTTP_200_OK
            )

        except ObjectDoesNotExist:
            return Response(
                status=status.HTTP_204_NO_CONTENT
            )
        except Exception as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserApi(APIView):

    def post(self, request):
        try:
            if request.method == 'POST':
                # POST request
                print('request', request)
                username = request.data.get('username')
                password = request.data.get('password')
                print('data: ', username, password)
                res = UserService().get_by_username(username=username, password=password)

                return res

        except ObjectDoesNotExist:
            return Response(
                status=400,
                data={'error': 'Invalid credentials'}
            )
        except Exception as ex:
            return Response(
                data=str(ex),
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class HomeApi(APIView):
    def get(self, request):
        return HttpResponse("Welcome to the homepage!")
