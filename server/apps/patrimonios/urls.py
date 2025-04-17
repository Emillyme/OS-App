from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatrimonioViewSet

router = DefaultRouter()
router.register(r'', PatrimonioViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]
