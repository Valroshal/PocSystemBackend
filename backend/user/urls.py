from django.urls import path, include

from backend.user.api.user import UserApi
from backend.user.views.user_view import info
app_label = 'user'

api_patterns = [
    path('user/', UserApi.as_view()),
]

ui_patterns = [
    path(
        route='info',
        view=info,
        name='info'
    ),
]

urlpatterns = [
    path('', include(api_patterns)),
    path('ui/', include(ui_patterns)),
]
