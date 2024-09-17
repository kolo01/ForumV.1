from django.http import HttpResponse

from rest_framework.response import Response
from rest_framework import status


from rest_framework import viewsets
from api.models.forum_model import ForumModel
from api.serializers.forum_serializer import ForumSerializer


class ForumViewSet(viewsets.ModelViewSet):
    queryset = ForumModel.objects.all()
    serializer_class = ForumSerializer
    http_method_names=["get", "post"]

    
        

