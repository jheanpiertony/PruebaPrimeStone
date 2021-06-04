"""
Definition of urls for PruebaGerardo.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms
from api import views
from rest_framework_simplejwt import views as jwt_views
from rest_framework import routers



"""Se registan las rutas para el api rest framework"""

router = routers.DefaultRouter()
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'cursos', views.CursoViewSet)
router.register(r'direcciones', views.DireccionViewSet)



"""Se registan las rutas para el traer el token y la ruta del admin de django"""

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('', admin.site.urls),
]
