from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, ResourceType, ResourceSet, ResourceSetComponent, Request, Resource


class SchedulerAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class SchedulerTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ResourceTypeSerializer(ShaniModelSerializer):
    class Meta:
        model = ResourceType
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ResourceSetSerializer(ShaniModelSerializer):
    class Meta:
        model = ResourceSet
        fields = org_model_base_fields + ['name', 'summary', 'description', 'attachments', ]


class ResourceSetComponentSerializer(ShaniModelSerializer):
    class Meta:
        model = ResourceSetComponent
        fields = org_model_base_fields + ['resource_set', 'type', 'count', ]


class RequestSerializer(ShaniModelSerializer):
    class Meta:
        model = Request
        fields = org_model_base_fields + ['requester', 'name', 'resource_set', 'priority', 'start_time', 'end_time',
                                          'purpose', 'status', 'attachments', ]


class ResourceSerializer(ShaniModelSerializer):
    class Meta:
        model = Resource
        fields = org_model_base_fields + ['type', 'name', 'summary', 'description', 'assigned_to', 'attachments',
                                          'properties', ]


serializer_map = {
    Attachment: SchedulerAttachmentSerializer,
    Tag: SchedulerTagSerializer,
    ResourceType: ResourceTypeSerializer,
    ResourceSet: ResourceSetSerializer,
    ResourceSetComponent: ResourceSetComponentSerializer,
    Request: RequestSerializer,
    Resource: ResourceSerializer,
}
