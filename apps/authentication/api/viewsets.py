from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_jwt import views as jwt_views 




class Login(APIView):
    serializer_class = LoginSerializer
    
    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        password =  request.data.get('password', None)
        
        user = authenticate(username=email, password=password)
        
        if (user):
            data_serialized = self.serializer_class(user)
            return Response(data_serialized.data, 200)
        return Response({"message":"user credentials invalid"},401)


class VerifyToken(jwt_views.VerifyJSONWebToken):
    def post(self, request, *args, **kwargs):
        data = super().post(request, *args, **kwargs)    
        return Response(data.data)
    
class RefreshToken(jwt_views.RefreshJSONWebToken):
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    


    
    
