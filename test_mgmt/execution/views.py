from rest_framework import viewsets, permissions

from api.views import default_search_fields, default_ordering, id_fields_filter_lookups, string_fields_filter_lookups, \
    datetime_fields_filter_lookups, compare_fields_filter_lookups, exact_fields_filter_lookups
from .models import Attachment, Tag, Release, Environment, ReliabilityRun, Defect, Run, ExecutionRecord
from .serializers import AttachmentSerializer, TagSerializer, ReleaseSerializer, EnvironmentSerializer, \
    ReliabilityRunSerializer, DefectSerializer, RunSerializer, ExecutionRecordSerializer


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


class ReleaseViewSet(viewsets.ModelViewSet):
    queryset = Release.objects.all()
    serializer_class = ReleaseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class DefectViewSet(viewsets.ModelViewSet):
    queryset = Defect.objects.all()
    serializer_class = DefectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'summary', 'description', 'external_id', 'release', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'description': string_fields_filter_lookups,
        'external_id': string_fields_filter_lookups,

        'release': id_fields_filter_lookups,
        'release__name': string_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'time', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'time': datetime_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class ExecutionRecordViewSet(viewsets.ModelViewSet):
    queryset = ExecutionRecord.objects.all()
    serializer_class = ExecutionRecordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'status', 'acceptance_test', 'automated', 'run', 'time', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        # 'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        # 'summary': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'acceptance_test': exact_fields_filter_lookups,
        'automated': exact_fields_filter_lookups,
        'defects': id_fields_filter_lookups,
        'run': id_fields_filter_lookups,
        'time': datetime_fields_filter_lookups,
        # 'testcase': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class ReliabilityRunViewSet(viewsets.ModelViewSet):
    queryset = ReliabilityRun.objects.all()
    serializer_class = ReliabilityRunSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                       'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                       'targetIPTE', 'ipte', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'build': string_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'start_time': datetime_fields_filter_lookups,
        'modified_time': datetime_fields_filter_lookups,
        'testName': string_fields_filter_lookups,
        'testEnvironmentType': string_fields_filter_lookups,
        'testEnvironmentName': string_fields_filter_lookups,
        'status': id_fields_filter_lookups,
        'targetIPTE': compare_fields_filter_lookups,
        'incidents': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }


class EnvironmentViewSet(viewsets.ModelViewSet):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    search_fields = default_search_fields
    ordering_fields = ['id', 'name', 'summary', 'type', 'purpose', 'current_release', 'org_group', ]
    ordering = default_ordering
    filterset_fields = {
        'id': id_fields_filter_lookups,
        'name': string_fields_filter_lookups,
        'summary': string_fields_filter_lookups,
        'type': string_fields_filter_lookups,
        'purpose': string_fields_filter_lookups,
        'current_release': id_fields_filter_lookups,
        'org_group': id_fields_filter_lookups,
    }
