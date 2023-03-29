from rest_framework import viewsets, permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups, exact_fields_filter_lookups
from automation.models import Step, Attachment
from automation.serializers import StepSerializer, AttachmentSerializer


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


class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'feature', 'org_group', 'name', 'expected_results', 'eta', 'tags', 'test_design_owner',
                       'test_design_status', 'automation_owner', 'automation_code_reference', 'automation_status', ]
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
    }
