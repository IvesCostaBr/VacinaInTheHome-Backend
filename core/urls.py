from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# from authentication.controllers import UserController, UserPublicController
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = routers.DefaultRouter()
# router.register(r'auth/users', UserController, basename='authentication')
# router.register(r'users', UserPublicController, basename='authentication')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('authentication/', include('authentication.urls')),
    path('auth/token/', TokenObtainPairView.as_view()),
    path('auth/token/refresh', TokenRefreshView.as_view()),
    path('auth/token/verify', TokenVerifyView.as_view()),
]
