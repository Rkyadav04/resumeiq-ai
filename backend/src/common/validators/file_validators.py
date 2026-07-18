"""
Reusable file validators.

These validators are generic and can be reused across multiple
modules such as resumes, jobs, certificates, and portfolios.
"""

from pathlib import Path

from django.core.exceptions import ValidationError


def validate_non_empty_file(file) -> None:
    """
    Ensure the uploaded file is not empty.
    """
    if file.size == 0:
        raise ValidationError("Uploaded file cannot be empty.")


def validate_file_size(file, max_size: int) -> None:
    """
    Validate maximum allowed file size.

    Args:
        file:
            Uploaded file object.

        max_size:
            Maximum size in bytes.
    """
    if file.size > max_size:
        raise ValidationError(
            f"File size exceeds the maximum allowed size of {max_size} bytes."
        )


def validate_file_extension(file, allowed_extensions: set[str]) -> None:
    """
    Validate uploaded file extension.

    Example:

        {".pdf", ".docx"}
    """
    extension = Path(file.name).suffix.lower()

    if extension not in allowed_extensions:
        raise ValidationError(
            f"Unsupported file type '{extension}'. "
            f"Allowed types: {', '.join(sorted(allowed_extensions))}"
        )