from rest_framework.decorators import api_view
from rest_framework.views import Response
from .models import CustomUser
from .serializers import CustomUserViewSerializer

# Create your views here.
@api_view(["GET"])
def getContactList(request, id):
    user = CustomUser.objects.get(id = id)

    if user == request.user:
        contacts = CustomUserViewSerializer(user.contacts, many=True).data
        return Response(contacts)
    else:
        return Response(
            {
                "detail": "You do not have permission to perform this action."
            }
        )
