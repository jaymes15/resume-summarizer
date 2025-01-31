from django.urls import include, path
from rest_framework.routers import DefaultRouter

from resumes import views
from resumes.apps import ResumesConfig

router = DefaultRouter()
router.register("resumes", views.ResumeViewSet, basename="resumes")
router.register("upload-resume", views.UploadResumeViewSet, basename="resumes")

app_name = ResumesConfig.name

urlpatterns = [path("", include(router.urls))]
