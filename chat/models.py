from django.db import models

from accounts.models import CustomUser

class Conversation(models.Model):
    name = models.TextField(null=True)
    TYPES = [
        ("i", "individual"),
        ("g", "group")
    ]
    type = models.CharField(choices=TYPES, max_length=1)
    users = models.ManyToManyField(CustomUser, related_name="conversations")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_archived = models.BooleanField(default=False)


class Message(models.Model):
    text = models.TextField()
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.RESTRICT)
    user = models.ForeignKey(CustomUser, related_name="messages", on_delete=models.RESTRICT)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)