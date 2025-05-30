from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignUpView, LogoutAPIView, SignUpAdminView, AllUsersView, UserDetails


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),     
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signupadmin/', SignUpAdminView.as_view(), name='signup_admin'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('', AllUsersView.as_view(), name='Users'),
    path('<int:pk>', UserDetails.as_view(), name='Users_details'),
] 