from rest_framework import viewsets
from .models import Gestor
from .serializers import GestorSerializer

class GestorViewSet(viewsets.ModelViewSet):
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer