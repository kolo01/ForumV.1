from django.http import HttpResponse
from rest_framework import viewsets
from api.models.message_model import MessageModel
from api.serializers.message_serializer import MessageSerializer

from rest_framework.response import Response
from rest_framework import status

class MessageViewSet(viewsets.ModelViewSet):
    queryset = MessageModel.objects.all()
    serializer_class = MessageSerializer
    http_method_names=["get", "post"]

    def list(self, request):
        id = request.GET.get('subject')
        
        if id is None:
            messages = MessageModel.objects.all()
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
        else:
            messages = MessageModel.objects.filter(sujet=id)
            print(messages)
            serializer = MessageSerializer(messages, many=True)
            return Response(serializer.data)
