from django.contrib.auth.models import User, Group
from rest_framework import serializers

from api.models import UseCase, Requirement, TestCase, Feature, Run, ExecutionRecord, Attachment, Defect, Release, \
    Epic, Sprint, Story, UseCaseCategory, ReliabilityRun, OrgGroup, Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Environment


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


class OrgGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroup
        fields = ['id', 'name', 'summary', 'auth_group', 'description', 'parent_org_group', 'leader', 'attachments', ]


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'employee_id', 'auth_user', 'role', 'org_group', 'attachments', 'org_group', ]  #


class ReleaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Release
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class EngineerOrgGroupParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = ['id', 'engineer', 'org_group', 'role', 'capacity', ]


class SiteHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = ['id', 'name', 'date', 'summary', 'attachments', 'org_group', ]


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['id', 'engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', ]


class EpicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Epic
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'release', 'org_group', ]


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'epic', 'org_group', ]


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'number', 'release', 'start_date', 'end_date', 'org_group', ]


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'name', 'summary', 'description', 'weight', 'attachments', 'rank', 'sprint', 'feature',
                  'org_group', ]


class UseCaseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCaseCategory
        fields = ['id', 'name', 'summary', 'description', 'weight', 'org_group', ]


class UseCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UseCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'weight', 'consumer_score', 'serviceability_score',
                  'test_confidence', 'development_confidence', 'category', 'requirements', 'attachments', 'org_group', ]


# class UseCaseStepSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Step
#         fields = ['id', 'summary', 'description', 'actor', 'interface', 'action']


class RequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirement
        fields = ['id', 'name', 'summary', 'description', 'use_cases', 'org_group', ]


class TestCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCase
        fields = ['id', 'name', 'summary', 'description', 'status', 'acceptance_test', 'automated', 'use_case',
                  'requirements', 'attachments', 'org_group', ]  # 'execution_status', 'defects'


class DefectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defect
        fields = ['id', 'summary', 'description', 'external_id', 'release', 'org_group', ]


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = ['id', 'build', 'name', 'time', 'release', 'org_group', ]


class ExecutionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExecutionRecord
        fields = ['id', 'name', 'summary', 'description', 'status', 'acceptance_test', 'automated', 'defects', 'run',
                  'time', 'org_group', ]


class ReliabilityRunSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReliabilityRun
        fields = ['id', 'build', 'name', 'start_time', 'modified_time', 'testName', 'testEnvironmentType',
                  'testEnvironmentName', 'status', 'totalIterationCount', 'passedIterationCount', 'incidentCount',
                  'targetIPTE', 'ipte', 'incidents', 'release', 'org_group', ]


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = ['id', 'name', 'summary', 'type', 'description', 'purpose', 'attachments', 'current_release',
                  'org_group', ]
