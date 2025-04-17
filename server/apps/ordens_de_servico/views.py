from rest_framework import viewsets
from .models import OrdemServico
from .serializers import OrdensServicosSerializer

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdensServicosSerializer