"""
Resume module constants.

This module centralizes all constants used across the Resume domain,
making the application easier to maintain and configure.
"""

from pathlib import Path

# ==============================================================================
# Upload Configuration
# ==============================================================================

RESUME_UPLOAD_DIR = "resumes"

# Maximum upload size (5 MB)
MAX_RESUME_SIZE = 5 * 1024 * 1024

# ==============================================================================
# Supported File Types
# ==============================================================================

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
}

ALLOWED_CONTENT_TYPES = {
    "application/pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
}

# ==============================================================================
# Text Extraction
# ==============================================================================

SUPPORTED_TEXT_EXTRACTION_EXTENSIONS = {
    ".pdf",
    ".docx",
}

# ==============================================================================
# Default Values
# ==============================================================================

DEFAULT_ENCODING = "utf-8"