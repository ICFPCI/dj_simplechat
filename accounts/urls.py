from django.urls import path, include
from rest_framework import routers
from .viewsets import CustomUserViewset
from .views import getContactList


router = routers.SimpleRouter()
router.register("profile", CustomUserViewset, basename="users")

urlpatterns = [
    path("profile/<int:id>/contacts/", getContactList),
    path("", include(router.get_urls())),
]
