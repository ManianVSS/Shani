from rest_framework import viewsets
from rest_framework.response import Response

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, \
    ShaniOrgGroupViewSet, datetime_fields_filter_lookups
from .models import Step, Attachment, Tag, MockAPI
from .serializers import StepSerializer, AttachmentSerializer, TagSerializer, MockAPISerializer
from django.db.models import Q

class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class StepViewSet(ShaniOrgGroupViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'feature', 'org_group', 'created_at', 'updated_at', 'published', 'name',
                       'expected_results', 'eta', 'tags', 'test_design_owner', 'test_design_status', 'automation_owner',
                       'automation_code_reference', 'automation_status', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'feature': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'expected_results': string_fields_filter_lookups,
        'eta': compare_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'test_design_owner': id_fields_filter_lookups,
        'test_design_status': id_fields_filter_lookups,
        'automation_owner': id_fields_filter_lookups,
        'automation_code_reference': string_fields_filter_lookups,
        'automation_status': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class MockAPIViewSet(ShaniOrgGroupViewSet):
    queryset = MockAPI.objects.all()
    serializer_class = MockAPISerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'http_method', 'status', 'org_group', 'created_at', 'updated_at', 'published', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'http_method': exact_fields_filter_lookups,
        'status': compare_fields_filter_lookups,
        'content_type': string_fields_filter_lookups,
    }


# noinspection PyMethodMayBeStatic
class MockAPIRoutingViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for mocking api.
    """

    def list(self):
        queryset = MockAPI.objects.all()
        serializer = MockAPISerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        queryset = MockAPI.objects.filter(Q(name=pk) & Q())
        serializer = MockAPISerializer(queryset, many=True)
        pass

    def retrieve(self, request, pk=None):
        return Response(data={'pk': pk}, status=200)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
