from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GestorViewSet

router = DefaultRouter()
router.register(r'', GestorViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
