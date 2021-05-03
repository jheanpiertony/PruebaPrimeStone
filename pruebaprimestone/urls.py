"""pruenaprimestone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from common import views
from front.views import HomeView


# API routes
router = routers.DefaultRouter()
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('front/', include('front.urls', namespace='front')),
    path('common/', include(router.urls)),
    path('', HomeView.as_view(), name='home'),
    path('api/token/', obtain_jwt_token, name='token_obtain_pair'),
    path('api/token/refresh/', refresh_jwt_token, name='token_refresh'),
]
