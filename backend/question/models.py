import uuid

from django.db import models


class QuestionModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
