import uuid

from django.db import models
from question.models import QuestionModel


class AnswerModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    question = models.ForeignKey(
        to=QuestionModel, on_delete=models.PROTECT, blank=False
    )
