from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import UseCase, Requirement, TestCase, Feature, Run, ExecutionRecord, Attachment, Defect, Release, \
    Epic, Sprint, Story, UseCaseCategory


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file']


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', ]


class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'release']


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'epic']


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'number', 'release', 'start_date', 'end_date']


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint', 'feature']


class UseCaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseCategory
        fields = ['id', 'name', 'summary', 'description', 'weight', ]


class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'weight', 'consumer_score', 'serviceability_score',
                  'test_confidence', 'development_confidence', 'category', 'requirements', 'attachments']


# class UseCaseStepSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Step
#         fields = ['id', 'summary', 'description', 'actor', 'interface', 'action']


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'name', 'summary', 'description', 'use_cases']


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'acceptance_test', 'automated', 'use_case',
                  'requirements', 'attachments', ]  # 'execution_status', 'defects'


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ['id', 'summary', 'description', 'external_id', 'release']


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'build', 'name', 'time', 'release']


class ExecutionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = ['id', 'name', 'summary', 'description', 'status', 'acceptance_test', 'automated', 'defects', 'run',
                  'time', ]


class ReliabilityRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                  'testEnvironmentName', 'status',
                  'totalIterationCount', 'passedIterationCount', 'incidentCount', 'targetIPTI', 'ipti', 'incidents',
                  'release']
