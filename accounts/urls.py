from django.urls import path, include
# from .views import CustomUserListApiView
from .viewsets import CustomUserViewset
from rest_framework import routers

import accounts.views as views

router = routers.SimpleRouter()
router.register("profile", CustomUserViewset, basename="users")

urlpatterns = [
    path("", include(router.get_urls())),
]
