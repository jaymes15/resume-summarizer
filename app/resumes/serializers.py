from rest_framework import serializers

from core.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    """Resume model serializer"""

    class Meta(object):
        model = Resume
        fields = ("id", "resume", "summary")
        read_only_fields = ("id", "resume", "summary")


class UploadResumeSerializer(serializers.ModelSerializer):
    """Resume model serializer for resume upload"""

    class Meta(object):
        model = Resume
        fields = ("id", "resume")
        read_only_fields = ("id",)
    
    def create(self, validated_data):
        return Resume.objects.create(summary="", **validated_data)


