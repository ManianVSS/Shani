from rest_framework import serializers

from .models import Attachment, Tag, ResourceType, ResourceSet, ResourceSetComponent, Request, Resource


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ResourceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceType
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ResourceSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSet
        fields = ['id', 'name', 'summary', 'description', 'attachments', 'org_group', 'created_at', 'updated_at',
                  'published', 'is_public', ]


class ResourceSetComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceSetComponent
        fields = ['id', 'resource_set', 'type', 'count', 'org_group', 'created_at', 'updated_at',
                  'published', 'is_public', ]


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'requester', 'name', 'resource_set', 'priority', 'start_time', 'end_time', 'purpose', 'status',
                  'attachments', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'type', 'name', 'summary', 'description', 'assigned_to', 'attachments', 'org_group',
                  'created_at', 'updated_at', 'published', 'is_public', ]


serializer_map = {
    Attachment: AttachmentSerializer,
    Tag: TagSerializer,
    ResourceType: ResourceTypeSerializer,
    ResourceSet: ResourceSetSerializer,
    ResourceSetComponent: ResourceSetComponentSerializer,
    Request: RequestSerializer,
    Resource: ResourceSerializer,
}
