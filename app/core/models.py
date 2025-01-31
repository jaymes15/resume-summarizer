import threading

from django.db import models
from django.utils.translation import gettext_lazy as _
from core.integrations.defaults import default_resume_summarizer, default_extract_resume_text
from core.utils import resume_file_path
from core.validators import validate_pdf_file


class Resume(models.Model):
    """Resume model"""
    resume = models.FileField(
        upload_to=resume_file_path,
        validators=[validate_pdf_file]
    )
    summary = models.TextField(blank=True, null=True)  # Store AI-generated summary

    class Meta:
        verbose_name_plural = "Resumes"

    def __str__(self):
        return str(self.resume.name)

    def process_summarization(self):
        """Runs LLM summarization in a separate thread."""
        extracted_text = default_extract_resume_text(self.resume)

        if extracted_text:
            name, summary = default_resume_summarizer(extracted_text)
            
            # Save the results asynchronously to avoid blocking
            Resume.objects.filter(id=self.id).update(
                summary=f"{name} \n\n {summary}"
            )

    def save(self, *args, **kwargs):
        """Override save method to extract text and process summarization asynchronously."""
        super().save(*args, **kwargs) 
        
        # Run summarization in a separate thread
        summarization_thread = threading.Thread(target=self.process_summarization)
        summarization_thread.start()
