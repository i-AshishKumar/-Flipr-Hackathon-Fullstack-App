from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.exceptions import ValidationError
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import RegisterSerializer, UserSerializer


# Create your views here.
# Register API
# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # return Response({
        # "user": UserSerializer(user, context=self.get_serializer_context()).data,
        # "token": x
        # })
        AuthToken.objects.create(user)[1]
        login(request, user)
        return redirect('/')

# Login API
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (TokenAuthentication,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False) == False:
            return redirect('/notregistered')
        user = serializer.validated_data['user']
        login(request, user)
        AuthToken.objects.create(user)[1]
        # return super(LoginAPI, self).post(request, format=None)
        return redirect('/')

class LogoutView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request, *args, **kwargs):
        # get the current token
        token = AuthToken.objects.get(user=request.user)
        # delete the token
        token.delete()
        logout(request)
        
        # # return success message
        # return Response({"message":"Successfully logged out."}, status=200)
        return redirect('/')

# def log_out(request):
#     logout(request)
#     return redirect('/')

# Get User API
class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user