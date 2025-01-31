from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models
from core.utils import resume_file_path
from core.validators import validate_pdf_file

class Resume(models.Model):
    """Resume model"""
    resume = models.FileField(
        upload_to=resume_file_path, 
        validators=[validate_pdf_file]
    )
    summary = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Resumes"

    def __str__(self):
        return str(self.resume.name)
