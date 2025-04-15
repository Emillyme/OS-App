from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpView, LogoutAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),     
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout/', LogoutAPIView.as_view(), name='logout')
] 