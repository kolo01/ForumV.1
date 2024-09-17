from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .viewsets.forum_viewset import ForumViewSet
from .viewsets.message_viewset import MessageViewSet
from .viewsets.topic_viewset import TopicViewSet

router = routers.DefaultRouter()
router.register(r'forum', ForumViewSet)
router.register(r'message', MessageViewSet)
router.register(r'topic', TopicViewSet)





urlpatterns = [
    path('', include(router.urls)),
]