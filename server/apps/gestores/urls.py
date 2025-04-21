from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GestorViewSet, UploadExcelView

router = DefaultRouter()
router.register(r'', GestorViewSet) 

urlpatterns = [
    path('upload/', UploadExcelView.as_view(), name='uploads'),
    path('', include(router.urls)),
]
