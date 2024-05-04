from rest_framework import serializers
from .models import Conversation, Message
from accounts.serializers import CustomUserViewSerializer

class MessageSerializer(serializers.ModelSerializer):
    user = CustomUserViewSerializer()
    class Meta:
        model = Message
        fields = "__all__"

class ConversationSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only = True)
    users = CustomUserViewSerializer(many=True, read_only = True)
    class Meta:
        model = Conversation
        fields = "__all__"

class ArchivedConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ["id", "name", "type", "is_archived"]