from rest_framework import viewsets
from .models import Manutentor
from apps.areas.models import Area
from apps.gestores.models import Gestor
from .serializers import ManutentorSerializer
import openpyxl
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

class ManutentorViewSet(viewsets.ModelViewSet):
    queryset = Manutentor.objects.all()
    serializer_class = ManutentorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['area', 'gestor', 'sn_manu', 'nome_manu']

class UploadExcelView(APIView):
    def post(self, request):
        excel_file = request.FILES.get('file')

        if not excel_file:
            return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                sn, manutentor, email, area_nome, gestor_nome = row
                area, _ = Area.objects.get_or_create(nome=area_nome)
                gestor, _ = Gestor.objects.get_or_create(nome=gestor_nome)

                Manutentor.objects.create(sn_manu=sn, nome_manu=manutentor, email=email, area=area, gestor=gestor)

            return Response({"message": "Dados importados com sucesso!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)