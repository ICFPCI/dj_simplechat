from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async, async_to_sync
import json

from .models import Conversation, Message
from .serializers import ArchivedConversationSerializer, MessageSerializer


class Consumer(AsyncJsonWebsocketConsumer):

    @database_sync_to_async
    def send_message(self, message_data):
                    
        if message_data.get("text", None) == None:
            raise Exception("No se ha proporcionado el texto del mensaje")
        
        if message_data.get("conversation_id", None) == None:
            raise Exception("No se ha proporcionado el id de la conversacion")

        message = Message()

        message.user_id = (self.scope["user"]).id
        message.text = message_data.get("text")
        message.conversation_id = message_data.get("conversation_id")
        message.save()

        serialized_message = MessageSerializer(message).data

        for user in message.conversation.users.all():
            async_to_sync(self.channel_layer.group_send)(
                str(user.id),
                {
                    "type": "message_event",
                    "event_type": "new-message",
                    "data": serialized_message,
                },
            )

    @database_sync_to_async
    def archive_message(self, message_data):
        
        if message_data.get("conversation_id", None) == None:
            raise Exception("No se ha proporcionado el id de la conversacion")
        
        conversation = Conversation.objects.get(id = message_data.get("conversation_id", None))
        conversation.is_archived = True
        conversation.save()

        serialized_conversation = ArchivedConversationSerializer(conversation).data

        async_to_sync(self.channel_layer.group_send)(
            str((self.scope["user"]).id),
            {
                "type": "message_event",
                "event_type": "conversation-archived",
                "data": serialized_conversation,
            },
        )


    async def connect(self):
        await self.channel_layer.group_add(str((self.scope["user"]).id), self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        return self.close(code)

    async def receive(self, text_data=None, bytes_data=None, **kwargs):
        json_data = json.loads(text_data)
        event_type = json_data.get("type", None)

        match event_type:
            case "ping":
                message = json_data.get("message", None)
                await self.channel_layer.group_send(
                    str((self.scope["user"]).id),
                    {
                        "type": "message_event",
                        "event_type": "pong",
                        "data": message,
                    },
                )

            case "double":
                try:
                    number = int(json_data.get("number", None))
                    doubled = number * 2
                    await self.send_json({"result": doubled})
                except Exception as e:
                    await self.send_json(
                        {
                            "error": str(e),
                            "message": "An error occurred while trying to double the provided number.",
                        }
                    )

            case "send-message":
                try:
                    message_data = json_data.get("message")
                    await self.send_message(message_data)
                except Exception as e:
                    await self.channel_layer.group_send(
                        str((self.scope["user"]).id),
                        {
                            "type": "message_event",
                            "event_type": "error-message",
                            "data": e,
                        },
                    )

            case "archive-conversation":
                try:
                    message_data = json_data.get("message")
                    await self.archive_message(message_data)
                except Exception as e:
                    print("error -> ", e)
                    await self.channel_layer.group_send(
                        str((self.scope["user"]).id),
                        {
                            "type": "message_event",
                            "event_type": "error-message",
                            "data": e,
                        },
                    )

            case _:
                await self.send_json(
                    content={
                        "error": "Event does not exist",
                        "message": f"The event type {event_type} is not recognized by the server.",
                    }
                )

    async def message_event(self, event):
        event_type = event["event_type"]
        data = event["data"]

        text_data = json.dumps({
            'type': event_type,
            'data': data
        })

        await self.send(text_data=text_data)
