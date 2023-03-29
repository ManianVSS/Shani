from rest_framework import viewsets, permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups, exact_fields_filter_lookups
from .models import Attachment, Tag, TestCaseCategory, TestCase
from .serializers import AttachmentSerializer, TagSerializer, TestCaseCategorySerializer, TestCaseSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class TestCaseCategoryViewSet(viewsets.ModelViewSet):
    queryset = TestCaseCategory.objects.all()
    serializer_class = TestCaseCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'weight', 'parent', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'weight': compare_fields_filter_lookups,
        'parent': id_fields_filter_lookups,
        'tags': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,

    }


class TestCaseViewSet(viewsets.ModelViewSet):
    queryset = TestCase.objects.all()
    serializer_class = TestCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'parent', 'status', 'type', 'external_id', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'type': id_fields_filter_lookups,
        'tags': id_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,

    }
