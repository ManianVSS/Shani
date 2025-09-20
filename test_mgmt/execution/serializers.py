from api.models import org_model_base_fields
from api.serializers import ShaniModelSerializer
from .models import Attachment, Tag, Release, Build, Defect, Run, ReliabilityIncident, ReliabilityRun, ExecutionRecord, \
    ReliabilityIteration, Environment


class ExecutionAttachmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Attachment
        fields = org_model_base_fields + ['name', 'file', ]


class ExecutionTagSerializer(ShaniModelSerializer):
    class Meta:
        model = Tag
        fields = org_model_base_fields + ['name', 'summary', 'description', ]


class ExecutionReleaseSerializer(ShaniModelSerializer):
    class Meta:
        model = Release
        fields = org_model_base_fields + ['name', 'summary', 'description', 'properties', 'attachments', ]


class BuildSerializer(ShaniModelSerializer):
    class Meta:
        model = Build
        fields = org_model_base_fields + ['release', 'name', 'type', 'build_time', 'summary', 'description',
                                          'properties', 'attachments', ]


class DefectSerializer(ShaniModelSerializer):
    class Meta:
        model = Defect
        fields = org_model_base_fields + ['release', 'build', 'summary', 'description', 'external_id', 'details_file',
                                          'attachments', ]


class RunSerializer(ShaniModelSerializer):
    class Meta:
        model = Run
        fields = org_model_base_fields + ['release', 'build', 'name', 'start_time', 'end_time', ]


class ExecutionRecordSerializer(ShaniModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = org_model_base_fields + ['name', 'summary', 'description', 'status', 'defects', 'run', 'start_time',
                                          'end_time', ]


class ReliabilityRunSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityRun
        fields = org_model_base_fields + ['release', 'build', 'name', 'type', 'start_time', 'modified_time', 'testName',
                                          'testEnvironmentType', 'testEnvironmentName', 'status', 'totalIterationCount',
                                          'passedIterationCount', 'incidentCount', 'targetIPTE', 'ipte', ]


class ReliabilityIterationSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityIteration
        fields = org_model_base_fields + ['run', 'name', 'index', 'status', 'start_time', 'end_time', 'results', ]


class ReliabilityIncidentSerializer(ShaniModelSerializer):
    class Meta:
        model = ReliabilityIncident
        fields = org_model_base_fields + ['release', 'build', 'run', 'iteration', 'defect', 'summary', 'description',
                                          'triaged', 'details_file', 'attachments', ]


class EnvironmentSerializer(ShaniModelSerializer):
    class Meta:
        model = Environment
        fields = org_model_base_fields + ['name', 'summary', 'type', 'description', 'assigned_to', 'purpose',
                                          'details_file', 'attachments', 'current_release', 'current_build',
                                          'properties', ]


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
