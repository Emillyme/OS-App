from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet, UploadExcelView

router = DefaultRouter()
router.register(r'', AmbienteViewSet) 

urlpatterns = [
    path('upload/', UploadExcelView.as_view(), name='uploads'),
    path('', include(router.urls)),
]
