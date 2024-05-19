from rest_framework import viewsets

from .models import Conversation, Message
from .serializers import ConversationSerializer, MessageSerializer
from .permissions import ConversationPermission

class ConversationViewset(viewsets.ModelViewSet):
    serializer_class = ConversationSerializer
    permission_classes = (ConversationPermission,)

    def get_queryset(self):
        user = self.request.user
        return Conversation.objects.prefetch_related("users", "messages", "messages__user").filter(users__id = user.id)

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.select_related("user", "conversation").all()
    serializer_class = MessageSerializer