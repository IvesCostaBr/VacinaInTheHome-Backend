from django.urls import path
from .api import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', viewsets.UserViewset, basename='user')

urlpatterns = [
    path("users/create/", viewsets.CreateUser.as_view()),
]

urlpatterns = router.urls