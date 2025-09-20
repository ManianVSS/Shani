from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, Release, Build, Defect, Run, ReliabilityIncident, ReliabilityRun, ExecutionRecord, \
    ReliabilityIteration, Environment


class ExecutionAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class ExecutionTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ExecutionReleaseSerializer(ShaniModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'properties', 'attachments', 'org_group', 'created_at',
                  'updated_at', 'published', ]


class BuildSerializer(ShaniModelSerializer):
    class Meta:
        model = Build
        fields = ['id', 'release', 'name', 'type', 'build_time', 'summary', 'description', 'properties', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class DefectSerializer(ShaniModelSerializer):
    class Meta:
        model = Defect
        fields = ['id', 'release', 'build', 'summary', 'description', 'external_id', 'details_file', 'attachments',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class RunSerializer(ShaniModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'release', 'build', 'name', 'start_time', 'end_time', 'org_group', 'created_at', 'updated_at',
                  'published', ]


class ExecutionRecordSerializer(ShaniModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = ['id', 'name', 'summary', 'description', 'status', 'defects', 'run', 'start_time', 'end_time',
                  'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class ReliabilityRunSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityRun
        fields = ['id', 'release', 'build', 'name', 'type', 'start_time', 'modified_time', 'testName',
                  'testEnvironmentType', 'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount',
                  'incidentCount', 'targetIPTE', 'ipte', 'org_group', 'created_at', 'updated_at', 'published',
                  'is_public', ]


class ReliabilityIterationSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityIteration
        fields = ['id', 'run', 'name', 'index', 'status', 'start_time', 'end_time', 'results', 'org_group',
                  'created_at', 'updated_at', 'published', 'is_public', ]


class ReliabilityIncidentSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityIncident
        fields = ['id', 'release', 'build', 'run', 'iteration', 'defect', 'summary', 'description', 'triaged',
                  'details_file', 'attachments', 'org_group', 'created_at', 'updated_at', 'published', 'is_public', ]


class EnvironmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'name', 'summary', 'type', 'description', 'assigned_to', 'purpose', 'details_file',
                  'attachments', 'current_release', 'current_build', 'properties', 'org_group', 'created_at',
                  'updated_at',
                  'published', ]


serializer_map = {
    Attachment: ExecutionAttachmentSerializer,
    Tag: ExecutionTagSerializer,
    Release: ExecutionReleaseSerializer,
    Build: BuildSerializer,
    Defect: DefectSerializer,
    Run: RunSerializer,
    ExecutionRecord: ExecutionRecordSerializer,
    ReliabilityIncident: ReliabilityIncidentSerializer,
    ReliabilityRun: ReliabilityRunSerializer,
    ReliabilityIteration: ReliabilityIterationSerializer,
    Environment: EnvironmentSerializer,
}
