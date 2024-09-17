from rest_framework import serializers
from api.models.topic_model import TopicModel


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicModel
        fields = '__all__'