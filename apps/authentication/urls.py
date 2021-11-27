from django.urls.conf import path
from .api import viewsets


urlpatterns = [
    path("login/", viewsets.Login.as_view()),
    path("verify/", viewsets.VerifyToken.as_view()),
    path("refresh/", viewsets.RefreshToken.as_view())
]