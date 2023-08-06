from django.urls import path
from users.views import (
    UserTokenObtainPairView, UserTokenRefreshView, UserTokenVerifyView,
    RegisterUserCreateAPIView, ActivationUserGenericAPIView, PasswordResetGenericAPIView,
    PasswordResetConfirmUpdateAPIView, SeenCreateAPIView, SeenListAPIView
)

app_name = 'users'
urlpatterns = [
    path('token/create/', UserTokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', UserTokenVerifyView.as_view(), name='token_verify'),
    path('register/', RegisterUserCreateAPIView.as_view(), name='register'),
    path('activated-account/', ActivationUserGenericAPIView.as_view(), name='activated_account'),
    path('reset-password/', PasswordResetGenericAPIView.as_view(), name='reset_password'),
    path('reset-password-confirm/', PasswordResetConfirmUpdateAPIView.as_view(), name='reset_password_confirm'),
    path('seen/create/<int:bird_id>', SeenCreateAPIView.as_view(), name='seen_create'),
    path('seen/list/', SeenListAPIView.as_view(), name='seen_list'),
]
