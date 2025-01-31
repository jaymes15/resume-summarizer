"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("resumes.urls")), 
    path("api/users/", include("users.urls")),
      path(
        "api_docs/",
        include_docs_urls(
            title="Resume Summarizer API",
            description="Resume Summarizer  API documentation",
        ),
    ),
    path(
        "api/schema/",
        get_schema_view(
            title="Resume Summarizer  API Schema",
            description="Resume Summarizer  API schema",
            version="1.0.0",
        ),
        name="api_schema",
    ),
    
] + (static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
     + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))
