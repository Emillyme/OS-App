from rest_framework import viewsets
from .models import Patrimonio
from .serializers import PatrimonioSerializer
import openpyxl
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

class PatrimonioViewSet(viewsets.ModelViewSet):
    queryset = Patrimonio.objects.all()
    serializer_class = PatrimonioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['ni', 'localizacao']

class UploadExcelView(APIView):
    def post(self, request):
        excel_file = request.FILES.get('file')

        if not excel_file:
            return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                ni, descricao, localizacao = row
                Patrimonio.objects.create(ni=ni, descricao=descricao, localizacao=localizacao)
            
            return Response({"message": "Dados importados com sucesso!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)