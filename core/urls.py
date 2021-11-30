from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('apps.authentication.urls')),
    path('', include('apps.user.urls')),
    path('', include('apps.agendamento.urls')),
    path('connect/token/',obtain_jwt_token)
]
