from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Person, House, User

from djoser.serializers import UserCreateSerializer, UserSerializer

class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'url', 'name', 'email', 'dob', 'age')

class HouseSerializer(HyperlinkedModelSerializer):
    # url = HyperlinkedIdentityField(view_name="myapp:user-detail")
    class Meta:
        model = House
        fields = ('url', 'id' ,'loc', 'owner', 'pin')

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        field = ('id', 'email', 'username', 'password', 'first_name', 'last_name')