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
            serializer.save()
            return Response({'message': 'Usuário criado com sucesso!'}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutAPIView(APIView):
        permission_classes = [IsAuthenticated] 

        def post(self,request):
            return Response({"message": "Logout realizado com sucesso!"}, status=200)

# class Soma(APIView):
#     def post(self, request):
#         permission_classes = [AllowAny]

#         a = request.data.get("a")
#         b = request.data.get("b")

#         if a is None or b is None:
#             return Response({"erro": "Você precisa enviar A e B"},
#             status=status.HTTP_400_BAD_REQUEST                
#             )

#         soma = a + b
#         return Response({"soma": soma})