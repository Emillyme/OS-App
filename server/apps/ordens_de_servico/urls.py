from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrdemServicoViewSet

router = DefaultRouter()
router.register(r'', OrdemServicoViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]
