from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Attachment, OrgGroup, Properties


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class OrgGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroup
        fields = ['id', 'name', 'summary', 'auth_group', 'description', 'org_group', 'leaders', 'created_at',
                  'updated_at', 'published', ]


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', ]


class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['id', 'name', 'details', 'org_group', 'created_at', 'updated_at', 'published', ]
