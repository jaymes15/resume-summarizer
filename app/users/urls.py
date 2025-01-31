from django.urls import path
from .views import UserCreateAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('token', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', UserCreateAPIView.as_view(), name='user-register'),
]