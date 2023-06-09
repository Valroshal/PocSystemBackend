"""poc_systems_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from backend import views

admin.autodiscover()


urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_products/', views.ProductApi.as_view()),
    path('update_product/', views.ProductApi.as_view()),
    path('user/', views.UserApi.as_view()),
    path('', views.HomeApi.as_view()),
    path('create_product/', views.ProductApi.as_view())

]
