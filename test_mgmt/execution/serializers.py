from rest_framework import serializers

from .models import Attachment, Tag, Release, Environment, ReliabilityRun, ExecutionRecord, Run, Defect


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', 'published', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'published', ]


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'published', ]


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ['id', 'summary', 'description', 'external_id', 'release', 'details_file', 'attachments',
                  'org_group', 'published', ]


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'build', 'name', 'time', 'release', 'org_group', 'published', ]


class ExecutionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = ['id', 'name', 'summary', 'description', 'status', 'acceptance_test', 'automated', 'defects', 'run',
                  'time', 'org_group', 'published', ]


class ReliabilityRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliabilityRun
        fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                  'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                  'targetIPTE', 'ipte', 'incidents', 'release', 'org_group', 'published', ]


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'name', 'summary', 'type', 'description', 'purpose', 'details_file', 'attachments',
                  'current_release', 'org_group', 'published', ]
