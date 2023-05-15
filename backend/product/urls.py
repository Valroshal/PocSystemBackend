from django.urls import path, include

from backend.product.api.product_api import ProductApi
from backend.product.views.product_view import info
app_label = 'product'

api_patterns = [
    # path('update_product/<str:product_id>', ProductApi.as_view()),
    path('get_products/', ProductApi.as_view()),
]

# ui_patterns = [
#     path(
#         route='info',
#         view=info,
#         name='info'
#     ),
# ]

urlpatterns = [
    path('', include(api_patterns)),
    # path('ui/', include(ui_patterns)),
]
