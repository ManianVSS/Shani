from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, \
    ShaniOrgGroupViewSet, datetime_fields_filter_lookups, compare_fields_filter_lookups, \
    org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Tag, ResourceType, ResourceSet, ResourceSetComponent, Request, Resource
from .serializers import SchedulerAttachmentSerializer, SchedulerTagSerializer, ResourceTypeSerializer, \
    RequestSerializer, \
    ResourceSetSerializer, ResourceSetComponentSerializer, ResourceSerializer


class SchedulerAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = SchedulerAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class SchedulerTagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = SchedulerTagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ResourceTypeViewSet(ShaniOrgGroupViewSet):
    queryset = ResourceType.objects.all()
    serializer_class = ResourceTypeSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ResourceSetViewSet(ShaniOrgGroupViewSet):
    queryset = ResourceSet.objects.all()
    serializer_class = ResourceSetSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ResourceSetComponentViewSet(ShaniOrgGroupViewSet):
    queryset = ResourceSetComponent.objects.all()
    serializer_class = ResourceSetComponentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'resource_set': fk_fields_filter_lookups,
        'type': fk_fields_filter_lookups,
        'count': compare_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class RequestViewSet(ShaniOrgGroupViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['resource_set', 'start_time', 'priority', 'end_time', 'requester', 'status', 'purpose',
                       'name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'requester': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'resource_set': fk_fields_filter_lookups,
        'priority': compare_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'end_time': datetime_fields_filter_lookups,
        'purpose': string_fields_filter_lookups,
        'status': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ResourceViewSet(ShaniOrgGroupViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['type', 'name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'assigned_to': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
