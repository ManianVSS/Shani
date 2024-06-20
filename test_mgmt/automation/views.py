import json

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups, exact_fields_filter_lookups, ShaniOrgGroupObjectLevelPermission, \
    ShaniOrgGroupViewSet, datetime_fields_filter_lookups
from .models import Step, Attachment, Tag, MockAPI, AuthenticatorSecret
from .serializers import StepSerializer, AttachmentSerializer, TagSerializer, MockAPISerializer, \
    AuthenticatorSecretSerializer


class AttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class TagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class StepViewSet(ShaniOrgGroupViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'feature', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', 'name',
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
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


class MockAPIViewSet(ShaniOrgGroupViewSet):
    queryset = MockAPI.objects.all()
    serializer_class = MockAPISerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'http_method', 'status', 'org_group', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'http_method': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'content_type': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
        'published': exact_fields_filter_lookups,
        'is_public': exact_fields_filter_lookups,
        'created_at': datetime_fields_filter_lookups,
        'updated_at': datetime_fields_filter_lookups,
    }


# noinspection PyMethodMayBeStatic
class MockAPIRoutingViewSet(viewsets.ViewSet):
    renderer_classes = (JSONRenderer,)
    """
    A simple ViewSet for mocking api.
    """

    def use_mock_api_route(self, request, pk, http_method, default_status_code=200,
                           default_content_type="application/json"):
        queryset = MockAPI.objects.filter(
            Q(name=pk) & Q(Q(http_method=http_method) | Q(http_method=MockAPI.HTTPMethod.ALL)))
        if queryset.exists():
            mock_api_impl = queryset.first()
            body = mock_api_impl.body if mock_api_impl.body else "{}"
            status = mock_api_impl.status if mock_api_impl.status else default_status_code
            content_type = mock_api_impl.content_type if mock_api_impl.content_type else default_content_type

            if content_type == "application/json":
                body = json.loads(body)
            return Response(data=body, status=status, content_type=content_type) \
                if mock_api_impl.content_type \
                else Response(data=body, status=status)
        else:
            return Response(status=404)

    def list(self, request):
        queryset = MockAPI.objects.all()
        serializer = MockAPISerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, pk=None):
        return self.use_mock_api_route(request, pk, MockAPI.HTTPMethod.POST, 201)

    def retrieve(self, request, pk=None):
        return self.use_mock_api_route(request, pk, MockAPI.HTTPMethod.GET)

    def update(self, request, pk=None):
        return self.use_mock_api_route(request, pk, MockAPI.HTTPMethod.PUT)

    def partial_update(self, request, pk=None):
        return self.use_mock_api_route(request, pk, MockAPI.HTTPMethod.PATCH)

    def destroy(self, request, pk=None):
        return self.use_mock_api_route(request, pk, MockAPI.HTTPMethod.DELETE)


class AuthenticatorSecretViewSet(ShaniOrgGroupViewSet):
    queryset = AuthenticatorSecret.objects.all()
    serializer_class = AuthenticatorSecretSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['id', 'issuer', 'user', 'initialized', 'org_group', 'created_at', 'updated_at', 'published',
                       'is_public', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'user': string_fields_filter_lookups,
        'secret': string_fields_filter_lookups,
        'issuer': string_fields_filter_lookups,
        'url': string_fields_filter_lookups,
        'initialized': exact_fields_filter_lookups,
    }
