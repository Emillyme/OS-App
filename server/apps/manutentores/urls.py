from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManutentorViewSet

router = DefaultRouter()
router.register(r'', ManutentorViewSet)  

urlpatterns = [
    path('', include(router.urls)),
]
