from django.urls import path, include
# from .views import CustomUserListApiView
from .viewsets import ConversationViewset, MessageViewset
from rest_framework import routers

router = routers.SimpleRouter()
router.register("conversation", ConversationViewset, basename="conversations")
router.register("message", MessageViewset, basename="messages")

urlpatterns = [
    path("", include(router.get_urls()))
]
