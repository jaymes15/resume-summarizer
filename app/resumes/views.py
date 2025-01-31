from rest_framework import mixins, permissions, viewsets

from core.models import Resume

from . import serializers


class ResumeViewSet(
    viewsets.GenericViewSet,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
):
    """Resume API endpoint"""
    permission_classes = (permissions.IsAdminUser,)

    queryset = Resume.objects.all()
    serializer_class = serializers.ResumeSerializer

  
class UploadResumeViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
):
    """Upload Resume API endpoint"""
    queryset = Resume.objects.all()
    serializer_class = serializers.UploadResumeSerializer

  