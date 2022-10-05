from rest_framework.permissions import BasePermission, IsAdminUser
# from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
# from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.viewsets import ModelViewSet
from .serializers import UserModelSerializer, BiographySerializer, BrendSerializer, UserSerializerWithIsSuperuserStaff

from .models import User, Brend, Biography


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  viewsets.GenericViewSet):
    # serializer_class = UserSerializer
    queryset = User.objects.all()

    # permission_classes = [StaffOnly]

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return UserSerializerWithIsSuperuserStaff
        return UserModelSerializer
    # permission_classes = [StaffOnly]


class BiographyViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializer


class BrendViewSet(ModelViewSet):
    queryset = Brend.objects.all()
    serializer_class = BrendSerializer
