from common.views import CreateListRetrieveViewSet
from django.contrib.auth.models import User
from user import serializers


class UserViewSet(CreateListRetrieveViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
