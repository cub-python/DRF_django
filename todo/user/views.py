from users_app.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from user.serializers import UserSerializerWithIsSuperuserStaff, UserModelSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerWithIsSuperuserStaff
        return UserModelSerializer
