from rest_framework import viewsets

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer

class ConversationViewset(viewsets.ModelViewSet):
    queryset = Conversation.objects.prefetch_related("users", "messages", "messages__user").all()
    serializer_class = ConversationSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user", "conversation").all()
    serializer_class = MessageSerializer