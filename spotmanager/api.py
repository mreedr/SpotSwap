from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie import fields
from spotmanager.models import Entry
from spotmanager.auth import UserObjectsOnlyAuthorization
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import ReadOnlyAuthorization
from django.contrib.auth.models import User

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user' #api slug reference
        fields = ['username', 'first_name', 'last_name', 'last_login']
        allowed_methods = ['get']
        authentication = BasicAuthentication()
        authorization = ReadOnlyAuthorization()
        serializer = Serializer(formats=['json', 'plist'])


class EntryResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')

    class Meta:
        queryset = Entry.objects.all()
        resource_name = 'entry'
        authentication = BasicAuthentication()
        authorization = Authorization()
        serializer = Serializer(formats=['json', 'plist'])
