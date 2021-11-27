from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_jwt.views import (
    obtain_jwt_token,refresh_jwt_token,verify_jwt_token
)

router = routers.DefaultRouter()

# router.register(r'users', viewsets.UserViewset, basename='user')

# router.register(r'auth/users', UserController, basename='authentication')
# router.register(r'users', UserPublicController, basename='authentication')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('authentication/', include('apps.authentication.urls')),
    path('', include('apps.user.urls')),
    path('connect/token/', obtain_jwt_token),
    path('connect/verify/', verify_jwt_token),
    path('connect/refresh/', refresh_jwt_token)
]
