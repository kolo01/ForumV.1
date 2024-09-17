from requests import Response
from rest_framework import viewsets
from api.models.topic_model import TopicModel
from api.serializers.topic_serializer import TopicSerializer

from rest_framework.response import Response
from rest_framework import status


class TopicViewSet(viewsets.ModelViewSet):
    queryset = TopicModel.objects.all()
    serializer_class = TopicSerializer
    http_method_names=["get", "post"]
        
    def list(self, request):
        id = request.GET.get('forum')
        
        if id is None:
            topics = TopicModel.objects.all()
            serializer = TopicSerializer(topics, many=True)
            return Response(serializer.data)
        else:
            topics = TopicModel.objects.filter(forum=id)
            serializer = TopicSerializer(topics, many=True)
            return Response(serializer.data)

  