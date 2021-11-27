from django.urls import path
from .api import viewsets
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'agendamentos', viewsets.AgendamentoViewSet, basename='agendamento')


urlpatterns = [
    
] + router.urls
