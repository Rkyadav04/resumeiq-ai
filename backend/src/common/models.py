"""
Common abstract models shared across the application.

These models provide reusable functionality such as UUID primary keys
and automatic timestamp management.
"""

import uuid

from django.db import models


class UUIDModel(models.Model):
    """
    Abstract model that provides a UUID primary key.
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """
    Abstract model that automatically tracks creation and update times.
    """

    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampedModel):
    """
    Base abstract model inherited by all business models.
    """

    class Meta:
        abstract = True