from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from user.serializers import UserModelSerializer
from .models import User, Brend, Biography


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UserSerializerWithIsSuperuserStaff(ModelSerializer):
    class Meta:
        model = UserModelSerializer
        fields = ('username','email','first_name','last_name','is_superuser', 'is_staff',)



class BiographySerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'


class BrendSerializer(ModelSerializer):

    class Meta:
        model = Brend
        fields = '__all__'
