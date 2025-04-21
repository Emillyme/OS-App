from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import SignUpSerializer

class SignUpView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=False,        # Usuário comum (sem acesso ao admin)
                is_superuser=False     # Usuário comum (sem permissões totais)
            )
    
            return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SignUpAdminView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True,        # Usuário comum (sem acesso ao admin)
                is_superuser=True     # Usuário comum (sem permissões totais)
            )
    
            return Response({'message': 'Usuário Admin criado com sucesso!'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignUpTecnicoView(APIView):
    def post(self, request):
        serializer = SignUpSerializer(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data['username']
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                is_staff=True,        # Usuário comum (sem acesso ao admin)
                is_superuser=False     # Usuário comum (sem permissões totais)
            )
    
            return Response({'message': 'Usuário Admin criado com sucesso!'}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
        permission_classes = [IsAuthenticated] 

        def post(self,request):
            return Response({"message": "Logout realizado com sucesso!"}, status=200)
