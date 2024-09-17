from django.db import models
from api.models.forum_model import ForumModel
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.

class TopicModel(DateTimeModel):
    forum = models.ForeignKey(ForumModel, on_delete=models.CASCADE, related_name='sujets')
    title = models.CharField(max_length=255)


    def __str__(self):
        return self.title

