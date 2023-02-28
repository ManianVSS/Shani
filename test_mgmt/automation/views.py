from django.shortcuts import render
from rest_framework import viewsets, permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    compare_fields_filter_lookups
from automation.models import Step
from automation.serializers import StepSerializer


# Create your views here.

class StepViewSet(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'description', 'eta', 'test_design_status', 'automation_status', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'eta': compare_fields_filter_lookups,
        'test_design_status': id_fields_filter_lookups,
        'automation_status': id_fields_filter_lookups,
    }
