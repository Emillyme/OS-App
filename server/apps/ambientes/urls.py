from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AmbienteViewSet

router = DefaultRouter()
router.register(r'', AmbienteViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
