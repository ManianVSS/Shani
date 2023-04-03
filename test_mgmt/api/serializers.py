from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Attachment, OrgGroup, Engineer, SiteHoliday, Leave, EngineerOrgGroupParticipation, Topic, \
    TopicEngineerAssignment, EngineerOrgGroupParticipationHistory, Site, Tag


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
        fields = ['id', 'name', 'file', 'org_group', 'published', ]


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ['id', 'name', 'summary', 'org_group', 'published', 'attachments', ]


class EngineerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engineer
        fields = ['id', 'employee_id', 'name', 'auth_user', 'role', 'org_group', 'published', 'site', 'attachments', ]


class EngineerOrgGroupParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngineerOrgGroupParticipation
        fields = ['id', 'engineer', 'org_group', 'published', 'role', 'capacity', ]


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
        fields = ['id', 'date', 'engineer', 'org_group', 'published', 'expected_capacity', 'capacity', ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'summary', 'description', 'org_group', 'published', ]


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'summary', 'description', 'parent_topic', 'org_group', 'published', ]


class TopicEngineerAssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicEngineerAssignment
        fields = ['id', 'topic', 'engineer', 'status', 'rating', 'start_date', 'end_date', 'org_group', 'published', ]
