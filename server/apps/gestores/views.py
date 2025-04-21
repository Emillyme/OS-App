from rest_framework import viewsets
from .models import Gestor
from .serializers import GestorSerializer
import openpyxl
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class GestorViewSet(viewsets.ModelViewSet):
    queryset = Gestor.objects.all()
    serializer_class = GestorSerializer

class UploadExcelView(APIView):
    def post(self, request):
        excel_file = request.FILES.get('file')

        if not excel_file:
            return Response({"error": "Nenhum arquivo enviado."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            wb = openpyxl.load_workbook(excel_file)
            sheet = wb.active

            for row in sheet.iter_rows(min_row=2, values_only=True):
                sn, nome, cargo = row
                Gestor.objects.create(sn_gest=sn, nome=nome, cargo=cargo)
            
            return Response({"message": "Dados importados com sucesso!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)