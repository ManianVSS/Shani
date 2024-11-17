from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Attachment, OrgGroup, Configuration, Site


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined',
                  'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', ]


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']


class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['id', 'name', 'value', 'description', 'created_at', 'updated_at', 'published', 'is_public', ]


class OrgGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroup
        fields = ['id', 'name', 'summary', 'auth_group', 'description', 'org_group', 'leaders', 'members', 'guests',
                  'consumers', 'created_at', 'updated_at', 'published', 'is_public', ]


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public',
                  'attachments', ]


serializer_map = {
    User: UserSerializer,
    Group: GroupSerializer,
    Configuration: ConfigurationSerializer,
    OrgGroup: OrgGroupSerializer,
    Attachment: AttachmentSerializer,
    Site: SiteSerializer,
}
