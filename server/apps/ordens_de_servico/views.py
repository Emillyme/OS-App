from rest_framework import viewsets
from .models import OrdemServico
from .serializers import OrdensServicosSerializer
from django_filters.rest_framework import DjangoFilterBackend

class OrdemServicoViewSet(viewsets.ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdensServicosSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'patrimonio', 'ambiente', 'manutentor', 'prioridade', 'funcionario', 'sn']