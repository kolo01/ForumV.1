from django.db import models
from api.models.topic_model import TopicModel
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.

class MessageModel(DateTimeModel):
    sujet = models.ForeignKey(TopicModel, on_delete=models.CASCADE, related_name='messages')
    content = models.TextField()

    def __str__(self):
        return f"Message in {self.sujet.title}"
