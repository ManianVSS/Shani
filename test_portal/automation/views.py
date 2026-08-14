import json

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, compare_fields_filter_lookups, exact_fields_filter_lookups, \
    ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, datetime_fields_filter_lookups, \
    enum_fields_filter_lookups, org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Tag, Step, Properties, MockAPI, ApplicationUnderTest, ApplicationPage, Element
from .serializers import AutomationAttachmentSerializer, AutomationTagSerializer, StepSerializer, PropertiesSerializer, \
    MockAPISerializer, \
    ApplicationUnderTestSerializer, ApplicationPageSerializer, ElementSerializer


class AutomationAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AutomationAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class AutomationTagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = AutomationTagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class StepViewSet(ShaniOrgGroupViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['feature', 'name', 'expected_results', 'eta', 'tags', 'status', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'feature': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'eta': compare_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class AutomationPropertiesViewSet(ShaniOrgGroupViewSet):
    queryset = Properties.objects.all()
    serializer_class = PropertiesSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class MockAPIViewSet(ShaniOrgGroupViewSet):
    queryset = MockAPI.objects.all()
    serializer_class = MockAPISerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'http_method', 'status', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'http_method': enum_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'content_type': enum_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


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


class ApplicationUnderTestViewSet(ShaniOrgGroupViewSet):
    queryset = ApplicationUnderTest.objects.all()
    serializer_class = ApplicationUnderTestSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = ['name', 'details', ]
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        # 'start_page': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ApplicationPageViewSet(ShaniOrgGroupViewSet):
    queryset = ApplicationPage.objects.all()
    serializer_class = ApplicationPageSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = ['name', 'details', ]
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'application': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        # 'check_element': fk_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class ElementViewSet(ShaniOrgGroupViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = ['name', 'details', 'locator_value', ]
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'page': fk_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'containing_element': fk_fields_filter_lookups,
        'element_type': enum_fields_filter_lookups,
        'locator_type': enum_fields_filter_lookups,
        'locator_value': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
