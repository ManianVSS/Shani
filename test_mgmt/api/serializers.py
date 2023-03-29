from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import UseCase, Requirement, Attachment, UseCaseCategory, OrgGroup, Engineer, SiteHoliday, Leave, \
    EngineerOrgGroupParticipation, Topic, TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Tag


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class OrgGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrgGroup
        fields = ['id', 'name', 'summary', 'auth_group', 'description', 'org_group', 'leaders', ]


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = ['id', 'name', 'file', 'org_group', ]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'summary', 'org_group', 'attachments', ]


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'org_group', 'site', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = ['id', 'engineer', 'org_group', 'role', 'capacity', ]


class SiteHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteHoliday
        fields = ['id', 'name', 'date', 'summary', 'attachments', 'site', ]


class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = ['id', 'engineer', 'start_date', 'end_date', 'summary', 'attachments', 'status', ]


class EngineerOrgGroupParticipationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipationHistory
        fields = ['id', 'date', 'engineer', 'org_group', 'expected_capacity', 'capacity', ]


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


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', ]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', ]


class TopicEngineerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicEngineerAssignment
        fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group', ]

