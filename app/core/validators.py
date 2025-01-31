from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_pdf_file(value):
    """Ensure that only PDF files are uploaded."""
    if not value.name.lower().endswith(".pdf"):
        raise ValidationError(_("Only PDF files are allowed."))
