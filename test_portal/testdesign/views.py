from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, fk_fields_filter_lookups, \
    string_fields_filter_lookups, compare_fields_filter_lookups, exact_fields_filter_lookups, \
    ShaniOrgGroupObjectLevelPermission, ShaniOrgGroupViewSet, datetime_fields_filter_lookups, \
    enum_fields_filter_lookups, org_model_view_set_filterset_fields, org_model_ordering_fields
from .models import Attachment, Tag, TestCaseCategory, TestCase
from .serializers import TestDesignAttachmentSerializer, TestDesignTagSerializer, TestCaseCategorySerializer, \
    TestCaseSerializer


class TestDesignAttachmentViewSet(ShaniOrgGroupViewSet):
    queryset = Attachment.objects.all()
    serializer_class = TestDesignAttachmentSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class TestDesignTagViewSet(ShaniOrgGroupViewSet):
    queryset = Tag.objects.all()
    serializer_class = TestDesignTagSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class TestDesignTestCaseCategoryViewSet(ShaniOrgGroupViewSet):
    queryset = TestCaseCategory.objects.all()
    serializer_class = TestCaseCategorySerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'weight', 'parent', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)


class TestDesignTestCaseViewSet(ShaniOrgGroupViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [ShaniOrgGroupObjectLevelPermission]
    search_fields = default_search_fields
    ordering_fields = ['name', 'summary', 'parent', 'status', 'type', 'external_id', ] + org_model_ordering_fields
    ordering = default_ordering
    filterset_fields = {
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': fk_fields_filter_lookups,
        'status': enum_fields_filter_lookups,
        'type': enum_fields_filter_lookups,
        'tags': exact_fields_filter_lookups,
        'use_cases': exact_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
    }.update(org_model_view_set_filterset_fields)
