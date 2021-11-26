from django.http.response import HttpResponse, HttpResponseNotFound, JsonResponse
from rest_framework import viewsets, permissions
from rest_framework import response
from rest_framework.decorators import action
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import LoginSerializer, UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import PublicUserPermission
from django.contrib.auth import authenticate


#TODO: Repensar arquitetura do controller User
class UserController(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes =  [JWTAuthentication]
    permission_classes =  [permissions.IsAuthenticated]
    http_method_names = ['get', 'post']
    
    def get_queryset(self) :
        if self.request.user.is_staff:
            return User.objects.all()
        
    def retrieve(self, request, *args, **kwargs):
        self.request.user
        instance = User.objects.get(pk=kwargs['pk'])
        return Response(UserSerializer(instance).data)

    #REVIEW: Refatorar maneira de verificação do usuario e sua resposta
    @action(detail=True, methods=['get'], 
            permission_classes=[permissions.IsAuthenticated, PublicUserPermission],
            url_path='get-user')
    def get_user(self, request, pk=True):
        user = User.objects.filter(pk=pk)
        if user.count() > 0 and user[0] == request.user: 
            return JsonResponse(UserSerializer(user[0]).data)
        return HttpResponseNotFound()
    
class UserPublicController(viewsets.ViewSet):
    @action(detail=False, methods=['post'], url_path='create-user')
    def create_user(self, request):
        return HttpResponse(200)
    

class CreateUser(APIView):
    def check_permissions(self, request):
        print("Fix um checagem aqui e já estou saindo")
        return super().check_permissions(request)

    def dispatch(self, request, *args, **kwargs):
        print("Executei o dispath")
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, format=None):
        return response.Response({"message":"entrei aqui"})


class Login(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer = self.serializer_class(user)
            return response.Response(serializer.data, status=200)
        return response.Response({"message":"credentials invalid!"}, status=401)
        


    


    
    
