from rest_framework import viewsets
from .models import Manutentor
from .serializers import ManutentorSerializer

class ManutentorViewSet(viewsets.ModelViewSet):
    queryset = Manutentor.objects.all()
    serializer_class = ManutentorSerializer