from rest_framework import viewsets, permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups
from .models import Attachment, Tag, FeatureCategory, Feature, Requirement, UseCase
from .serializers import AttachmentSerializer, TagSerializer, FeatureCategorySerializer, FeatureSerializer, \
    RequirementSerializer, UseCaseSerializer


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


class FeatureCategoryViewSet(viewsets.ModelViewSet):
    queryset = FeatureCategory.objects.all()
    serializer_class = FeatureCategorySerializer
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


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'parent', 'status', 'external_id', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'parent': id_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'tags': id_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,

    }


class UseCaseViewSet(viewsets.ModelViewSet):
    queryset = UseCase.objects.all()
    serializer_class = UseCaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'feature', 'status', 'weight', 'consumer_score',
                       'serviceability_score', 'test_confidence', 'development_confidence', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,

        'feature': id_fields_filter_lookups,
        'requirements': id_fields_filter_lookups,

        'weight': compare_fields_filter_lookups,
        'consumer_score': compare_fields_filter_lookups,
        'serviceability_score': compare_fields_filter_lookups,
        'test_confidence': compare_fields_filter_lookups,
        'development_confidence': compare_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class RequirementViewSet(viewsets.ModelViewSet):
    queryset = Requirement.objects.all()
    serializer_class = RequirementSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'use_cases': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }
