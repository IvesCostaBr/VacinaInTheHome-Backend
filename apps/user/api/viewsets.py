from django.http.response import HttpResponse
from rest_framework import response
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from ..models import User
from rest_framework import viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

 
class UserViewset(viewsets.ModelViewSet): 
    serializer_class = UserSerializer
    permission_class =[IsAuthenticated]
    authentication_class=[JSONWebTokenAuthentication]
    
    def get_queryset(self):
        if self.request.user.is_superuser:   
            return User.objects.all()
    
    def retrieve(self, request, pk=None):
        user = self.request.user
        instance = self.get_object()
        if user == instance:
            serializer = self.serializer_class(instance)
            return Response(serializer.data)
        return Response({"message":"operation not allowed"}, 403)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    
    
class CreateUser(APIView):
    def post(self, request):
        try:    
            user = User.objects.create_user(
                email=request.data.get('email'),
                password=request.data.get('password'),
                first_name=request.data.get('first_name'),
                last_name=request.data.get('last_name'),
                cpf=request.data.get('cpf'),
                card_sus=request.data.get('card_sus'),
            )
            if user.is_valid:  
                response_code = 201
            else:
                response_code = 500
        except:
            response_code = 500
            raise Exception("Erro ao cadastrar usuário")
            
        
        return HttpResponse(response_code)